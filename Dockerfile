FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt

#COPY . .

CMD