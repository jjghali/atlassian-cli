import pprint36 as pprint
from .jira_service import JiraService


class ConfluenceService:

    # DEFAULT_TEMPLATE_FILE_PATH = "../../templates/"

    releasenote_template = ""
    product_changelog_template = ""
    component_changelog_template = ""
    jiraService = JiraService()

    def __init__(self):
        self.load_releasenote_template()
        self.load_product_changelog_template()
        self.load_component_changelog_template()

    def generate_releasenote(self, project_key, version):
        versionData = self.jiraService.get_project_version_infos(
            project_key, version)
        releasenote = self.releasenote_template.replace(
            "%fixversion%", versionData["id"])
        releasenote = releasenote.replace("%project-key%", project_key)
        releasenote = releasenote.replace("%validate_task%", "tasks here")
        print(releasenote)
        # pass

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
