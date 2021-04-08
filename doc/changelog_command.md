# Changelog
## Description
Create a  changelog for a component or product page on Confluence
## Synopsis
```bash
$ atlcli [COMMON_ARGS] changelog [SUBCOMMAND] [OPTION]...
```
## Sub commands

| Name               | Description                                         | 
|--------------------|-----------------------------------------------------|
| generate-component | Creates the changelog for a component on confluence |
| generate-product   | Creates the changelog for a product on confluence   |

## Options and arguments
### generate-component
| Name                        | Mandatory | Description                                                |
|-----------------------------|-----------|------------------------------------------------------------|
| `-v, --version `            | Required  | Component/service version                                  |
| `-s, --space-key`           | Required  | Space key for the Confluence space                         |
| `-n, --component-name`      | Required  | Component name                                             |
| `-i, --parent-page-id`      | Required  | Id of the page under which you will create your changelogs |
| `-t, --template-file `      | Required  | Path to the template file for your changelog               |
| `--dry -run / --no-dry-run` | Optional  | Dry run for testing                                        |
| `--help`                    | Optional  | Show the help.                                             |

### generate-product
| Name                        | Mandatory | Description                                                |
|-----------------------------|-----------|------------------------------------------------------------|
| `-v, --version `            |           | Product version                                            |
| `-s, --space-key`           |           | Space key for the Confluence space                         |
| `-n, --product-name`        |           | Product name                                               |
| `-f, --configuration-repos` |           | Name of the repos where the configurations are stored      |
| `-j, --project-key`         |           | Project key used in your Jira project                      |
| `-i, --parent-page-id`      |           | Id of the page under which you will create your changelogs |
| `-t, --template-file `      |           | Path to the template file for your changelog               |
| `--dry-run / --no-dry-run`  |           | Dry run for testing                                        |
| `--help`                    |           | Show the help.                                             |

## Examples
### generate-component
```bash
$ atlcli --verifyssl \
         --jira-url=http://jira.contoso.com \
         --confluence-url=http://confluence.contoso.com \
         --bitbucket-url=http://bitbucket.contoso.com \
         --username=johnsmith \
         --password=super-password \
         changelog generate-component \
         --version=1.2.0 \
         --space-key=SPACE-CONTOSO \
         --project-key=CONTO \
         --parent-page-id=12345 \
         --template-file=tamplate-folter/template-component.gdlf
```
### generate-product
```bash
$ atlcli --verifyssl \
         --jira-url=http://jira.contoso.com \
         --confluence-url=http://confluence.contoso.com \
         --bitbucket-url=http://bitbucket.contoso.com \
         --username=johnsmith \
         --password=super-password \
         changelog generate-product \
         --version=0.0.1 \
         --space-key=SPACE-CONTOSO \
         --configuration-repos=https://bitbucket.contoso.com/scm/contoso/configuration.git
         --project-key=CONTO \
         --parent-page-id=12345 \
         --template-file=tamplate-folter/template-product.gdlf
```