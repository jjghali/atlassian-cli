# Usage guide

## Installation
### From pypi
For this type of installation you will only need to run the following command.
``` bash
$ pip install atlcli
```

### From the source code 
For this type of installation you will only need to run the following command. You will need to be in the root folder of the project in order to install it.
```
$ pip install .
```
You can also add `--editable` as an argument in case you want to debug the app.
```bash
pip install --editable .
```

## Usage
## Synopsis
```
atlcli [OPTION]... [COMMAND] [SUBCOMMAND] [OPTION]...
```

## Options and arguments
### **Application options**

|Name| Mandatory |Description|
|--|--|--|
|`--skipssl/--no-skipssl`|Optional|Skips ssl validation in case you have certificates issues (not recommended)|
|`--bitbucket-url`|Required| Bitbucket URL|
|`--jira-url`|Required| Jira URL|
|`--confluence-url`|Required| Confluence URL|
|`--username`|Required| Username to use for accessing Atlassian products|
|`--password`|Required|    Password to use for accessing Atlassian products|
|`--help`| Optional| Shows the help informations|

---
## Command and subcommand options
### Commands
|Name|Description|
|-|-|
|[changelog](./changelog_command.md)|    Creates a changelog page on Confluence|
|[component](./component_command.md)|    Get information about a component|
|[product](./product_command.md)|      Get information about a product|
|[releasenote](./releasenote_command.md)|  Creates a release note one on Confluence|
|[config](./config_command.md)|Creates a configuration file for local use of atlcli.|
|version|      App version|

## Examples
### Generate a release note
```bash
$ atlcli --skipssl \
        --jira-url=$JIRA_URL \
        --confluence-url=$CONFLUENCE_URL \
        --bitbucket-url=$BITBUCKET_URL \
        --username=$ATLASSIAN_USER \
        --password=$ATLASSIAN_PASSWORD \
        releasenote generate \
        --version=$VERSION_TAG \
        --space-key=$SPACE_KEY \
        --project-key=$JIRA_PROJECT_KEY \
        --parent-page-id=$PARENT_PAGE \
        --template-file=infra-resources/atlcli-templates/$TEMPLATE_FILE
```
