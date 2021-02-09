FROM python:3.9-alpine

# Install python packages
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Add current folder in /usr/src/app
ADD . /usr/src/app/atlassian-cli
RUN ls -ltra /usr/src/app/atlassian-cli/*