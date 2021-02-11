FROM python:3.9-alpine

# Install python packages
RUN mkdir /atlcli

COPY cli/ /atlcli/cli
COPY requirements.txt /atlcli/requirements.txt
COPY README.md /atlcli/README.md
COPY setup.py /atlcli/setup.py

WORKDIR /atlcli

WORKDIR /atlcli

RUN pip install .