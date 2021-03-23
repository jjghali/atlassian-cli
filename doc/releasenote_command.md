# Release note
## Description
Create a  release note for a component or product page on Confluence
## Synopsis
```bash
$ atlcli [COMMON_ARGS] releasenote [SUBCOMMAND] [OPTION]...
```
## Sub commands

|Name|Description|
|-|-|
|generate| Creates the release note for a product on confluence|

## Options and arguments
### generate
|Name|Mandatory|Description|
|-|-|-|
|`-v, --version `|Required|Release/Product version |
|`-s, --space-key`|Required|Space key for the Confluence space |
|`-j, --project-key`|Required|Project key used in your Jira project|
|`-i, --parent-page-id`|Required|Id of the page under which you will create your release notes|
|`-t, --template-file `|Required|Path to the template file for your release note|
|`--dry-run / --no-dry-run`|Optional|Dry run for testing|
|`--help`|Optional|Show the help.|

## Example
### generate
```bash
$ atlcli --verifyssl \
         --jira-url=http://jira.contoso.com \
         --confluence-url=http://confluence.contoso.com \
         --bitbucket-url=http://bitbucket.contoso.com \
         --username=johnsmith \
         --password=super-password \
         releasenote generate \
         --version=1.2.0 \
         --space-key=SPACE-CONTOSO \
         --project-key=CONTO \
         --parent-page-id=12345 \
         --template-file=tamplate-folter/template-component.gdlf
```
