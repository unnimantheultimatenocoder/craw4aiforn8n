[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
On this page
# Configure an external PostgreSQL database
Langflow's default database is [SQLite](https://docs.langflow.org/<https:/www.sqlite.org/docs.html>), but you can configure Langflow to use PostgreSQL instead.
This guide will walk you through the process of setting up an external database for Langflow by replacing the default SQLite connection string `sqlite:///./langflow.db` with PostgreSQL.
## Prerequisite[​](https://docs.langflow.org/<#prerequisite> "Direct link to Prerequisite")
  * A [PostgreSQL](https://docs.langflow.org/<https:/www.pgadmin.org/download/>) database


## Connect Langflow to PostgreSQL[​](https://docs.langflow.org/<#connect-langflow-to-postgresql> "Direct link to Connect Langflow to PostgreSQL")
To connect Langflow to PostgreSQL, follow these steps.
  1. Find your PostgreSQL database's connection string. It looks like `postgresql://user:password@host:port/dbname`. For example, if you started PostgreSQL with this Docker command:


`
_10
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres
`
Your connection string would be `postgresql://some-postgres:mysecretpassword@localhost:5432/postgres`.
  1. Create a `.env` file for configuring Langflow.


`
_10
touch .env
`
  1. To set the database URL environment variable, add it to your `.env` file:


`
_10
LANGFLOW_DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
`
tip
The Langflow project includes a `.env.example`[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/.env.example>) file to help you get started. You can copy the contents of this file into your own `.env` file and replace the example values with your own preferred settings. Replace the value for `LANGFLOW_DATABASE_URL` with your PostgreSQL connection string.
  1. Run Langflow with the `.env` file:


`
_10
langflow run --env-file .env
`
  1. In Langflow, create traffic by running a flow.
  2. Inspect your PostgreSQL deployment's tables and activity. You will see new tables and traffic created.


## Example Langflow and PostgreSQL docker-compose.yml[​](https://docs.langflow.org/<#example-langflow-and-postgresql-docker-composeyml> "Direct link to Example Langflow and PostgreSQL docker-compose.yml")
The Langflow project includes a `docker-compose.yml`[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/docker_example/docker-compose.yml>) file for quick deployment with PostgreSQL.
This configuration launches Langflow and PostgreSQL containers, with Langflow pre-configured to use the PostgreSQL database. Customize the database credentials as needed.
To start the services, navigate to the `/docker_example` directory, and then run `docker-compose up`.
`
_14
services:
_14
 langflow:
_14
  image: langflow-ai/langflow:latest
_14
  environment:
_14
   - LANGFLOW_DATABASE_URL=postgresql://user:password@postgres:5432/langflow
_14
  depends_on:
_14
   - postgres
_14
_14
 postgres:
_14
  image: postgres:15
_14
  environment:
_14
   - POSTGRES_USER=user
_14
   - POSTGRES_PASSWORD=password
_14
   - POSTGRES_DB=langflow
`
  * [Prerequisite](https://docs.langflow.org/<#prerequisite>)
  * [Connect Langflow to PostgreSQL](https://docs.langflow.org/<#connect-langflow-to-postgresql>)
  * [Example Langflow and PostgreSQL docker-compose.yml](https://docs.langflow.org/<#example-langflow-and-postgresql-docker-composeyml>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
