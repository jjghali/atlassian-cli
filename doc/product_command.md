# Product
## Description
 Get information about a product
## Synopsis
```bash
$ atlcli [COMMON_ARGS] product [SUBCOMMAND] [OPTION]...
```
## Sub commands

| Name       | Description                                  |
|------------|----------------------------------------------|
| `info`     | Displays info about a product                |
| `list`     | Lists all the deployed versions of a product |
| `tickets`  | Lists all components of a product            |
| `versions` | Lists all the deployed versions of a product |

## Options and arguments
### info
`NYI`

### **list**
`NYI`

### **tickets**
| Name                             | Mandatory | Description |
|----------------------------------|-----------|-------------|
| `-v, --product-version`          | Required  |             |
| `-j, --project-key`              | Required  |             |
| `--changes / --no-changes`       | Optional  |             |
| `--confluence / --no-confluence` | Optional  |             |

### **stats**
Displays statistics about a product and push data to a PowerBI Realtime dataset or produce a CSV file. It will give you the following informations:

    - Deployment frequency per version
    - Story points per version
    - Lead times per version
| Name                               | Mandatory |  Description                                                                |
|------------------------------------|-----------|-----------------------------------------------------------------------------|
| `-v', --version`                   | Optional  | Specify version if you want statistics about a version.                     |
| `-j', --project-key`               | Required  | Project key used in your Jira project.                                      |
| `--json/--no-json`                 | Optional  | Provides stats in json format.                                              |
| `-p', --powerbi-url`               | Optional  | Push data to a PowerBI Real Time Dataset if provided.                       |
| `--all-releases/--no-all-releases` | Optional  | Produces stats for all the releases created in a product. (Run it only once)|
| `--csv/--no-csv`                   | Optional  | Produces a csv file.                                                        |
| `-s', '--since`                    | Optional  | Specify start date for stats.                                               |

### versions
`NYI`

## Example
### info
```bash
NYI
```
### list
```bash
NYI
```
### tickets
```bash
NYI
```
### stats
#### **To PowerBI with all releases**
```bash
    atlcli \
    --skipssl \
    --jira-url=https://jira.contoso.com/ \
    --username=edward.elric \
    --password=alchemy123 \
    product \
    stats \
    --project-key=FMA \
    -p https://api.powerbi.com/beta/c5df3113-2028-401f-8efb-a96886ee6fd3datasets/57e73b32-21e3-4726-9958-862989efdad1/rokey=APIKEY \
    --all-releases \
    --since=2020/09/01

```

#### **To a CSV file with all releases**
```bash
    atlcli \
    --skipssl \
     --jira-url=https://jira.contoso.com/ \
    --username=edward.elric \
    --password=alchemy123 \
    product \
    stats \
    --project-key=FMA \                
    --all-releases \
    --since=2020/09/01 \
    --csv
```
