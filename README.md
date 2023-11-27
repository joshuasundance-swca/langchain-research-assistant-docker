# langchain-research-assistant-docker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

[![Push to Docker Hub](https://github.com/joshuasundance-swca/langchain-research-assistant-docker/actions/workflows/docker-hub.yml/badge.svg)](https://github.com/joshuasundance-swca/langchain-research-assistant-docker/actions/workflows/docker-hub.yml)
[![langchain-research-assistant-docker on Docker Hub](https://img.shields.io/docker/v/joshuasundance/langchain-research-assistant-docker?label=langchain-research-assistant-docker&logo=docker)](https://hub.docker.com/r/joshuasundance/langchain-research-assistant-docker)
[![Docker Image Size (tag)](https://img.shields.io/docker/image-size/joshuasundance/langchain-research-assistant-docker/latest)](https://hub.docker.com/r/joshuasundance/langchain-research-assistant-docker)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
![Known Vulnerabilities](https://snyk.io/test/github/joshuasundance-swca/langchain-research-assistant-docker/badge.svg)

This repo provides a docker setup to run the LangChain research-assistant template using langserve.

- [Relevant LangChain documentation](https://python.langchain.com/docs/templates/research-assistant)


- Example LangSmith traces
  - [_What is the average territory size of the Florida Scrub-Jay in Central Florida?_](https://smith.langchain.com/public/cf52fc9f-5800-4279-b61b-e15221d3a5e3/r)
  - [_Does SWCA Environmental Consultants use AI and data science?_](https://smith.langchain.com/public/fcae93da-b87e-49a6-992c-d5034bcf82e8/r)


## Quickstart

```bash
# clone the repo
git clone https://github.com/joshuasundance-swca/langchain-research-assistant-docker.git
cd langchain-research-assistant-docker

# make a .env file
cp .env.example .env
nano .env

# start the service
docker compose up
```


## Usage

- The service will be available at `http://localhost:8000`.
- You can access the OpenAPI documentation at `http://localhost:8000/docs` and `http://localhost:8000/openapi.json`.
- Access the Research Playground at `http://127.0.0.1:8000/research-assistant/playground/`.

- You can also use the `RemoteRunnable` class to interact with the service:

```python
from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/research-assistant")
```

See the [LangChain docs](https://python.langchain.com/docs/templates/research-assistant) for more information.
