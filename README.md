# langchain-research-assistant-docker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

This repo provides a docker setup to run the LangChain research-assistant template using langserve.

- [Relevant LangChain documentation](https://python.langchain.com/docs/templates/research-assistant)

- [Example LangSmith trace](https://smith.langchain.com/public/cf52fc9f-5800-4279-b61b-e15221d3a5e3/r)


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
