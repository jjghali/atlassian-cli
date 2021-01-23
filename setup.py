from setuptools import setup

deps = [
    'click',
    'atlassian-python-api',
    'pyyaml'
]


setup(
    name='gandalf',
    version='0.1',
    py_modules=['cli', "commands"],
    install_requires=deps,
    entry_points='''
        [console_scripts]
        gandalf=cli.app:cli
    ''',
)
