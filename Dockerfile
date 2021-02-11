FROM python:3.9-alpine

# Install python packages
COPY requirements.txt /requirements.txt
RUN pip install .