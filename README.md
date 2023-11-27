# langchain-research-assistant-docker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

- [Relevant LangChain documentation](https://python.langchain.com/docs/templates/research-assistant)

- [Example LangSmith trace](https://smith.langchain.com/public/cf52fc9f-5800-4279-b61b-e15221d3a5e3/r)


## Introduction

This repo provides a docker setup to run the LangChain research-assistant template using langserve.

The service provides various endpoints for interacting with the Research Assistant, including input and output schema endpoints, feedback, invoke, batch, and streaming functionalities.


## Try it out

1. Make a `.env` file and add at least `OPENAI_API_KEY`

```bash
cp .env.example .env
nano .env
```

2. Start the service

```bash
git clone https://github.com/joshuasundance-swca/langchain-research-assistant-docker.git
cd langchain-research-assistant-docker
docker compose up
```


## Usage

- The service will be available at `http://localhost:8000`.
- You can access the OpenAPI documentation at `http://localhost:8000/docs`.
- Access the Research Playground at `http://127.0.0.1:8000/research-assistant/playground/`.

- You can also use the `RemoteRunnable` class to interact with the service:

```python
from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/research-assistant")
```

See the [LangChain docs](https://python.langchain.com/docs/templates/research-assistant) for more information.
