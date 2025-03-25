# workshop-datascience-template

A sample project which shows how to work with the datascience template.

# Table of Contents

- [Setup](#setup)
- [Tooling](#cruft-and-cookiecutter)
- [Template Structure](#template-structure)
- [Get It Running Locally](#get-it-running-locally)
- [Get It Running Remotely](#get-it-running-remotely)

## Setup

To actively participate in the workshop, please install the following tools **before the session begins**. Please prefer using **winget** or another package manager (brew, apt, ...).

### Steps

#### 1. Install Git

Install the well known git client (CLI): 

Instructions: https://git-scm.com/downloads

#### 2. Install Visual Studio Code (VS Code)

Visual Studio Code is a lightweight yet powerful code editor with built-in support for development tools like Python, Docker, and Git. It is the recommended editor for working on workshop projects.

Instructions: https://code.visualstudio.com/

#### 3. Install Docker Desktop

Docker Desktop allows you to run containerized applications on your local machine. It's essential for running isolated and reproducible development environments during the workshop.

Instructions: https://docs.docker.com/desktop/setup/install/windows-install/

## Cruft and Cookiecutter

### Cookiecutter

What does it do?

- Generates directories and files from templates
- Uses Jinja2 templating to inject custom values (like project name, author, etc.)
- Works for any type of project (Python packages, Docker setups, web apps, etc.)

Why do we use them?

- Speed up project setup – one command can scaffold an entire ready-to-go project structure.
- Enforce best practices – you define your project architecture once, and reuse it consistently.
- Team-wide standardization – ensures everyone starts with the same structure.
- Supports prompts – ask the user questions (e.g. project name, license) to dynamically build out the template.

### Cruft

What does it do?

- Keeps metadata about where the template came from
- Lets you pull in updates from the upstream template (like bug fixes, new configs)
- Detects local modifications to avoid overwriting them

Why do we use it?

- Maintain template-based projects over time – like Git for project templates
- Avoid cruft (hence the name) – removes unused or obsolete template files

## Template Structure

```bash
tree -a . -I '.git'
.
├── .cruft.json
├── .devcontainer
│   ├── .env
│   ├── devcontainer.json
│   └── docker-compose.yml
├── .dockerignore
├── .editorconfig
├── .gitignore
├── Dockerfile
├── README.md
├── docs
│   ├── index.md
│   └── reference.md
├── mkdocs.yml
├── pyproject.toml
├── tests
│   ├── .gitkeep
│   └── test__example.py
└── workshop_datascience_template
    ├── __init__.py
    └── main.py
```

### Important files:

- **.gitignore:** List of files which will not be tracked by `git`
- **.cruft.json:** Contains metadata to when you initialized the template and any values set during the initial setup.
- **.editorconfig:** Default config for editors (tabs vs spaces)

#### Docs

- **docs/:** A folder container docs can be rendered using the mkdocs package (not python specific).
- **mkdocs.yml:** Configuration for creating and hosting docs -> results in HTML/CSS/JS

#### Devcontainer

- **.devcontainer:** Contains all files to setup devcontainers
- **.devcontainer/.env:** Default variables which can be public
- **.devcontainer:/devcontainer.json** Configuration for the devcontainers and setting up plugins
- **.devcontainer/docker-compose.yml:** The service configuration which starts the container

#### Docker

- **Dockerfile:** Build instructions for production and devcontainers.
- **.dockerignore.json:** List of ignored files when running `COPY` or `ADD` commands.

#### Python

- **poetry.lock and pyproject.toml:** Contains information about the python package and dependencies.

Ensure the python environment is correctly loaded using these commands in the vscode terminal:
```
# see if env is correctly set up
python --version  # should show 3.11
poetry show  # should show dependencies
python workshop_datascience_template/main.py  # executes an example script
```

## Get It Running Locally

Open the command palette and run "Open in container..." and wait for the build to complete successfully. 

## Accessing data

You can access data either mounting a directory from local host in you `docker-compose.yml` or use our own S3 service. You can find an example for configuring your own s3 service in:
`.devcontainer/.env-private.example` and in `notebooks/load_from_private_s3.py`

## Get It Running Remotely

## Services which are useful

### publicS3storage.risc-software.at


---

## SCRIPT

This are command executed for the demo

```bash
# ONLY FOR DEMO PURPOSES
git clone https://github.com/falknerdominik/workshop-datascience-template
# or if you want to create your own repository, answer the questions which pop up in your terminal
cruft create -f https://github.com/prescriptiveanalytics/python-package-template

# At this point the repository is finished and you can execute "Open in container...".
# CMD+SHIFT+P or CTRL+SHIFT+P to open the command palette and search for it

## Validate setup
# lock dependencies
git checkout template-structure
poetry lock
poetry install

# see if env is correctly set up
python --version  # should show 3.11
poetry show  # should show dependencies
python workshop_datascience_template/main.py  # executes an example script
# Use command palette to select correct interpreter (Python: Select interpreter)

## Penguins with script
# Restart your bash
git checkout penguins-script
poetry install
poetry add pandas scikit-learn seaborn matplotlib
python workshop_datascience_template/penguin_analysis.py
# cool - now we get prediction on the sex of the penguin (based on features such as mass and bill length/flipper length/...)

## Penguins with notebooks
# ...but the plot is missing - notebooks can help!
git checkout penguins-notebook
poetry install
poetry add ipykernel
# enable the vscode extensions in `.devcontainer/devcontainer.json` and rebuild
# open the notebook and execute cells with SHIFT+ENTER

## Accessing data
git checkout risc-s3
poetry install
poetry add cloudpathlib
# follow the instruction in the python notebook: `notebooks/load_from_private_s3.py`
# You can remotely load data from the public NAS!
```