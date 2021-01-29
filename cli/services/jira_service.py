import base64
import requests
import json
from atlassian import Jira
from utils import ConfigurationManager
import pprint36 as pprint


class JiraService:
    confManager = ConfigurationManager()

    def __init__(self):
        self.config = self.confManager.load_config()
        self.jiraInstance = Jira(
            url=self.config["jira-url"],
            username=self.config["credentials"]["username"],
            password=self.config["credentials"]["password"])

    def get_ticket(self, ticket_name):
        """get tickets basic infos"""
        pass

    def get_changelog(self, ticket_name):
        """get commits and repos changed linked to ticket"""
        issue_details = self.jiraInstance.issue(ticket_name)
        issue_id = issue_details["id"]
        changes = self.get_changes(issue_id)

    def get_repositories_from_issue(self, issue_id):
        endpoint_url = "{jira_url}/rest/dev-status/1.0/issue/detail".format(
            jira_url=self.config["jira-url"])

        querystring = {
            "issueId": issue_id,
            "applicationType": "stash",
            "dataType": "repository"
        }

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Basic {0}".format(self.config["credentials"]["base64"])
        }

        response = requests.request(
            "GET", endpoint_url, data=payload, headers=headers, params=querystring)
        result = json.loads(response.text)
        repositories = result["detail"][0]["repositories"]
        return repositories

    def get_project_version_infos(self, version):
        data = self.jiraInstance.get_project_versions_paginated(
            self.config["project-key"], limit=50)
        versionData = next(
            filter(lambda x: x["name"] == "{0}.{1}".format(
                self.config["project-key"], version), data["values"]), None)

        return versionData

    def get_project_version_issues(self, versionId):
        jql_query = "project = {0} AND fixVersion = {1} AND (type = Story OR type = Improvement ) order by key".format(
            self.config["project-key"], versionId)

        data = self.jiraInstance.jql(jql_query)["issues"]
        return data

    def printConfluenceMarkup(self, versionId):
        issues = self.get_project_version_issues(versionId)

        content = "|| Ticket JIRA || Projects || Status || Summary || Remarques ||\n"
        rows = ""
        for x in issues:
            repositories = self.get_repositories_from_issue(x["id"])
            concatRepos = ""

            if len(repositories) > 0:
                for r in repositories:
                    concatRepos = concatRepos + r["name"] + ", "

            if concatRepos is "":
                concatRepos = " "
            row = "||{ticket}|{repos}|{status}|{summary}|{remarques}|".format(
                ticket=x["key"], repos=concatRepos, status=x["fields"]["status"]["name"], summary=x["fields"]["summary"].replace("|", "-"), remarques=" ")
            rows = rows + row + "\n"

        content = content + rows
        return content
