A Flask Datatable Demo
================

This is a demo project. It utilizes tool including Flask, Docker, Javascript, Datatables, Bootstrap, CSS and etc.
I am planning on hosting it on AWS ECS service.

## Hierarchy

Descriptions of the folders and the files in the repo:

- Dockerfile: It contains all the commands to build a Docker image which includs Python, Flask and source code.
- makefile: To build the image using Dockerfile.
- requirements.txt: It lists all the Python packages that needs to be pip installed during the image building
- init_sh: Inside this folder, there is a bash script, init.sh. It is the script that runs in the first place once the Docker container starts running. It contains the command to start Flask.
- sample_table_docker: Source code is inside this folder. To break down:
  - same_table.py: Flask Python script
  - templates: HTML template that Flask uses to create a UI
  - static: static files UI uses, such as CSS and JS
- .gitignore: Tell git to ingore temporary or hidden files

