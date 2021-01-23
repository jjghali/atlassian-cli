# Gandalf
## Introduction
Gandalf is a Atlassian product CLI that allows you to create release notes, get infos about the repositories and repositories.
## Requirements
* Python 3.+
* Virtualenv
* PIP 3+

For ubuntu users:
```
$ sudo apt install python3 python3-pip
```
For other platforms
```
pip install virtualenv
```

## Project setup

In order to run the project you will first need to create a Virtual environment in python by running the following command.

```
pip install virtualenv
mkdir venv
python3 -m virtualenv ./venv
cd venv/bin
source activate
```

## Installing and adding pip dependencies
### Installing dependencies

After creating virtualenv you will need to install the requirements for the project. Go back to the root of the project and run the following command.

```
pip install -r requirements.txt
```
### Debug
```
pip install debugpy
python -m debugpy --listen 5678 cli/app.py
```

### Features
* Note de livraison qui affiche les etapes de livraison (comme les notes de livraison mpm)
* Changelog

### Addding pip dependencies
After adding a new module to the project you will need to update the requirements.txt file in order for it to have the new module. You cand do this by running the following command.

```
pip freeze > requirements.txt
```


## Doc
https://pypi.org/project/atlassian-python-api/
https://click.palletsprojects.com/en/7.x/