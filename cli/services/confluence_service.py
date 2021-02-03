import re
import ssl
import pprint36 as pprint
from datetime import datetime
from atlassian import Confluence
from .jira_service import JiraService
from utils import ConfigurationManager


class ConfluenceService:

    confManager = ConfigurationManager()

    releasenote_template = ""
    product_changelog_template = ""
    component_changelog_template = ""
    jiraService = JiraService()

    def __init__(self):

        self.config = self.confManager.load_config()

        if self.config is not None:
            self.confluence = Confluence(
                url=self.config["confluence-url"],
                username=self.config["credentials"]["username"],
                password=self.config["credentials"]["password"],
                verify_ssl=False
            )

            self.load_releasenote_template()
            self.load_product_changelog_template()
            self.load_component_changelog_template()

    def generate_releasenote(self, project_key, version):
        versionData = self.jiraService.get_project_version_infos(
            project_key, version)

        tasks = self.jiraService.printConfluenceMarkup(
            project_key, versionData["id"])

        releasenote = self.releasenote_template.replace(
            "%fixversion%", versionData["id"])
        releasenote = releasenote.replace("%project-key%", project_key)
        releasenote = releasenote.replace("%validate_task%", tasks)

        return releasenote

    def push_releasenote(self, spacekey, version, parent_page_id, releasenote):
        current_date = datetime.today().strftime("%Y-%m-%d")
        semantic_version = ""

        m = re.search(
            "(([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?)", version)

        if m:
            semantic_version = m.group(1)

        title = "{0} - {1}".format(semantic_version, current_date)

        converted_releasenote = self.confluence.convert_wiki_to_storage(
            releasenote)["value"]

        self.confluence.update_or_create(
            parent_page_id, title, converted_releasenote, representation='storage')

    # Converts content made with Confluence wiki markup to

    def load_releasenote_template(self):
        try:
            file = open("templates/releasenote-template.gdlf",
                        encoding='utf-8', mode="r")
            self.releasenote_template = file.read()

        except IOError:
            print("Releasenote template file is missing.")

    def load_product_changelog_template(self):
        pass

    def load_component_changelog_template(self):
        pass
