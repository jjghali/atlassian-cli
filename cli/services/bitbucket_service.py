import json
import re
import semantic_version
from atlassian import Bitbucket
from atlassian import Jira
from utils import ConfigurationManager

import pprint36 as pprint


class BitbucketService:

    # bitbucketInstance = None
    confManager = ConfigurationManager()

    def __init__(self):
        self.config = self.confManager.load_config()
        self.bitbucketInstance = Bitbucket(
            url=self.config["bitbucket-url"],
            username=self.config["credentials"]["username"],
            password=self.config["credentials"]["password"])

    def getRelease(self, component_name, version):

        result = self.bitbucketInstance.get_project_tags(self.config['product-name'],
                                                         component_name, version)
        tags = result["values"]
        target_tag = next(
            filter(lambda x: x["displayId"] == version, tags), None)
        previous_tag = self.getPreviousMajorRelease(tags, target_tag)
        changelog = self.bitbucketInstance.get_changelog(self.config['product-name'],
                                                         component_name,
                                                         previous_tag, target_tag, limit=1000)
        return changelog

    def filterMajorReleases(self, tags):
        filtered_tags = []
        pattern = re.compile(
            r"^([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?$")
        filtered_tags = list(
            filter(lambda x: pattern.match(x["displayId"]) is not None, tags))

        return filtered_tags

    def getPreviousMajorRelease(self, tags, version):
        filtered_tags = self.filterMajorReleases(tags)
        previous_release = None
        position = filtered_tags.index(version)

        if position > 0:
            previous_release = filtered_tags[position]
        return previous_release
