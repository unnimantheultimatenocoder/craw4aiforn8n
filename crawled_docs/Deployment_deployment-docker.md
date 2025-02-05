[Skip to main content](https://docs.langflow.org/Deployment/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/Deployment/</>)
[](https://docs.langflow.org/Deployment/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/Deployment/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/Deployment/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/Deployment/</>)
  * [Welcome to Langflow](https://docs.langflow.org/Deployment/</>)
  * [Get started](https://docs.langflow.org/Deployment/<#>)
  * [Starter projects](https://docs.langflow.org/Deployment/<#>)
  * [Tutorials](https://docs.langflow.org/Deployment/<#>)
  * [Concepts](https://docs.langflow.org/Deployment/<#>)
  * [Components](https://docs.langflow.org/Deployment/<#>)
  * [Agents](https://docs.langflow.org/Deployment/<#>)
  * [Configuration](https://docs.langflow.org/Deployment/<#>)
  * [Deployment](https://docs.langflow.org/Deployment/<#>)
    * [Docker](https://docs.langflow.org/Deployment/</Deployment/deployment-docker>)
    * [GCP](https://docs.langflow.org/Deployment/</deployment-gcp>)
    * [HuggingFace Spaces](https://docs.langflow.org/Deployment/</deployment-hugging-face-spaces>)
    * [Kubernetes](https://docs.langflow.org/Deployment/</deployment-kubernetes>)
    * [Railway](https://docs.langflow.org/Deployment/</deployment-railway>)
    * [Render](https://docs.langflow.org/Deployment/</deployment-render>)
  * [Integrations](https://docs.langflow.org/Deployment/<#>)
  * [Contributing](https://docs.langflow.org/Deployment/<#>)
  * [API reference](https://docs.langflow.org/Deployment/<#>)
  * [Changelog](https://docs.langflow.org/Deployment/<#>)


  * [](https://docs.langflow.org/Deployment/</>)
  * Deployment
  * Docker


On this page
# Docker
This guide will help you get LangFlow up and running using Docker and Docker Compose.
## Prerequisites[​](https://docs.langflow.org/Deployment/<#856bb2d98156402bbd1980365b98110c> "Direct link to Prerequisites")
  * Docker
  * Docker Compose


## Docker[​](https://docs.langflow.org/Deployment/<#55b5d304f2294e47b0dcd3e069cf5e67> "Direct link to Docker")
### Clone repo and build Docker container[​](https://docs.langflow.org/Deployment/<#ba89773aa8b8425b985bfe7ba91c35cc> "Direct link to Clone repo and build Docker container")
  1. Clone the LangFlow repository:
`git clone https://github.com/langflow-ai/langflow.git`
  2. Navigate to the `docker_example` directory:
`cd langflow/docker_example`
  3. Run the Docker Compose file:
`docker compose up`


LangFlow will now be accessible at `http://localhost:7860/`.
### Docker Compose configuration[​](https://docs.langflow.org/Deployment/<#02226209cad24185a6ec5b69bd820d0f> "Direct link to Docker Compose configuration")
The Docker Compose configuration spins up two services: `langflow` and `postgres`.
### LangFlow service[​](https://docs.langflow.org/Deployment/<#d749848451ea43bd86f6f096dc77e6e6> "Direct link to LangFlow service")
The `langflow` service uses the `langflowai/langflow:latest` Docker image and exposes port 7860. It depends on the `postgres` service.
Environment variables:
  * `LANGFLOW_DATABASE_URL`: The connection string for the PostgreSQL database.
  * `LANGFLOW_CONFIG_DIR`: The directory where LangFlow stores logs, file storage, monitor data, and secret keys.


Volumes:
  * `langflow-data`: This volume is mapped to `/app/langflow` in the container.


### PostgreSQL service[​](https://docs.langflow.org/Deployment/<#121140decbfe4997b12213bdd2c4da7e> "Direct link to PostgreSQL service")
The `postgres` service uses the `postgres:16` Docker image and exposes port 5432.
Environment variables:
  * `POSTGRES_USER`: The username for the PostgreSQL database.
  * `POSTGRES_PASSWORD`: The password for the PostgreSQL database.
  * `POSTGRES_DB`: The name of the PostgreSQL database.


Volumes:
  * `langflow-postgres`: This volume is mapped to `/var/lib/postgresql/data` in the container.


### Switch to a specific LangFlow version[​](https://docs.langflow.org/Deployment/<#2b3e191ea48f4feab89242433cf012d5> "Direct link to Switch to a specific LangFlow version")
If you want to use a specific version of LangFlow, you can modify the `image` field under the `langflow` service in the Docker Compose file. For example, to use version 1.0-alpha, change `langflowai/langflow:latest` to `langflowai/langflow:1.0-alpha`.
[PreviousSecurity best practices](https://docs.langflow.org/Deployment/</configuration-security-best-practices>)[NextGCP](https://docs.langflow.org/Deployment/</deployment-gcp>)
  * [Prerequisites](https://docs.langflow.org/Deployment/<#856bb2d98156402bbd1980365b98110c>)
  * [Docker](https://docs.langflow.org/Deployment/<#55b5d304f2294e47b0dcd3e069cf5e67>)
    * [Clone repo and build Docker container](https://docs.langflow.org/Deployment/<#ba89773aa8b8425b985bfe7ba91c35cc>)
    * [Docker Compose configuration](https://docs.langflow.org/Deployment/<#02226209cad24185a6ec5b69bd820d0f>)
    * [LangFlow service](https://docs.langflow.org/Deployment/<#d749848451ea43bd86f6f096dc77e6e6>)
    * [PostgreSQL service](https://docs.langflow.org/Deployment/<#121140decbfe4997b12213bdd2c4da7e>)
    * [Switch to a specific LangFlow version](https://docs.langflow.org/Deployment/<#2b3e191ea48f4feab89242433cf012d5>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
