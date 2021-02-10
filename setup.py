from _typeshed import NoneType
import os
from setuptools import setup, find_packages

deps = [
    'click',
    'atlassian-python-api',
    'pyyaml',
    'prettytable',
    'semantic-version',
    'pprint36',
    'requests'
]

version = ""

if os.getenv('RELEASE_VERSION') is NoneType:
    version = "dev"

setup(
    name='atlcli',
    version='0.1.0,
    packages=find_packages(),
    py_modules=['cli', "commands"],
    include_package_data=True,
    install_requires=deps,
    entry_points='''
        [console_scripts]
        atlcli=cli.app:cli
    ''',
)
