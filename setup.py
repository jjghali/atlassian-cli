<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import re
=======
from _typeshed import NoneType
>>>>>>> e781746... added dynamic version setting
=======

>>>>>>> 14cabeb... Update setup.py
=======
import re
>>>>>>> 7680c96... changed setup.py
import os
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

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
github_ref = os.getenv('GITHUB_REF')
if github_ref is not None:
    m = re.search(
        "(([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?)", github_ref)
    if m:
        version = m.group(1)
else:
    version = "dev"

setup(
    name='atlcli',
    version=version,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    py_modules=['cli', "commands"],
    include_package_data=True,
    install_requires=deps,
    entry_points='''
        [console_scripts]
        atlcli=cli.app:cli
    ''',
)
