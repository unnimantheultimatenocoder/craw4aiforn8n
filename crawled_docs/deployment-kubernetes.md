[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)![Langflow](https://docs.langflow.org/img/langflow-logo-white.svg)](https://docs.langflow.org/</>)
  * [Welcome to Langflow](https://docs.langflow.org/</>)
  * [Get started](https://docs.langflow.org/</get-started-installation>)
  * [Starter projects](https://docs.langflow.org/</starter-projects-basic-prompting>)
  * [Tutorials](https://docs.langflow.org/</tutorials-blog-writer>)
  * [Concepts](https://docs.langflow.org/</concepts-overview>)
  * [Components](https://docs.langflow.org/</components-agents>)
  * [Agents](https://docs.langflow.org/</agents-overview>)
  * [Configuration](https://docs.langflow.org/</configuration-api-keys>)
  * [Deployment](https://docs.langflow.org/</Deployment/deployment-docker>)
    * [Docker](https://docs.langflow.org/</Deployment/deployment-docker>)
    * [GCP](https://docs.langflow.org/</deployment-gcp>)
    * [HuggingFace Spaces](https://docs.langflow.org/</deployment-hugging-face-spaces>)
    * [Kubernetes](https://docs.langflow.org/</deployment-kubernetes>)
    * [Railway](https://docs.langflow.org/</deployment-railway>)
    * [Render](https://docs.langflow.org/</deployment-render>)
  * [Integrations](https://docs.langflow.org/</integrations-assemblyai>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Deployment
  * Kubernetes


On this page
# Kubernetes
This guide will help you get LangFlow up and running in Kubernetes cluster, including the following steps:
  * Install [LangFlow as IDE](https://docs.langflow.org/</deployment-kubernetes>) in a Kubernetes cluster (for development)
  * Install [LangFlow as a standalone application](https://docs.langflow.org/</deployment-kubernetes>) in a Kubernetes cluster (for production runtime workloads)


## LangFlow (IDE)[​](https://docs.langflow.org/<#cb60b2f34e70490faf231cb0fe1a4b42> "Direct link to LangFlow \(IDE\)")
This solution is designed to provide a complete environment for developers to create, test, and debug their flows. It includes both the API and the UI.
### Prerequisites[​](https://docs.langflow.org/<#3efd3c63ff8849228c136f9252e504fd> "Direct link to Prerequisites")
  * Kubernetes server
  * kubectl
  * Helm


### Step 0. Prepare a Kubernetes cluster[​](https://docs.langflow.org/<#290b9624770a4c1ba2c889d384b7ef4c> "Direct link to Step 0. Prepare a Kubernetes cluster")
We use [Minikube](https://docs.langflow.org/<https:/minikube.sigs.k8s.io/docs/start/>) for this example, but you can use any Kubernetes cluster.
  1. Create a Kubernetes cluster on Minikube.
`
_10
minikube start
`
  2. Set `kubectl` to use Minikube.
`
_10
kubectl config use-context minikube
`


### Step 1. Install the LangFlow Helm chart[​](https://docs.langflow.org/<#b5c2a35144634a05a392f7e650929efe> "Direct link to Step 1. Install the LangFlow Helm chart")
  1. Add the repository to Helm.
`
_10
helm repo add langflow <https://langflow-ai.github.io/langflow-helm-charts>
_10
helm repo update
`
  2. Install LangFlow with the default options in the `langflow` namespace.
`
_10
helm install langflow-ide langflow/langflow-ide -n langflow --create-namespace
`
  3. Check the status of the pods
`
_10
kubectl get pods -n langflow
`
`
_10
NAME                 READY  STATUS  RESTARTS    AGE
_10
langflow-0              1/1   Running  0       33s
_10
langflow-frontend-5d9c558dbb-g7tc9  1/1   Running  0       38s
`


### Step 2. Access LangFlow[​](https://docs.langflow.org/<#34c71d04351949deb6c8ed7ffe30eafb> "Direct link to Step 2. Access LangFlow")
Enable local port forwarding to access LangFlow from your local machine.
`
_10
kubectl port-forward -n langflow svc/langflow-langflow-runtime 7860:7860
`
Now you can access LangFlow at `http://localhost:7860/`.
### LangFlow version[​](https://docs.langflow.org/<#645c6ef7984d4da0bcc4170bab0ff415> "Direct link to LangFlow version")
To specify a different LangFlow version, you can set the `langflow.backend.image.tag` and `langflow.frontend.image.tag` values in the `values.yaml` file.
`
_10
langflow:
_10
 backend:
_10
  image:
_10
   tag: "1.0.0a59"
_10
 frontend:
_10
  image:
_10
   tag: "1.0.0a59"
`
### Storage[​](https://docs.langflow.org/<#6772c00af79147d293c821b4c6905d3b> "Direct link to Storage")
By default, the chart will use a SQLLite database stored in a local persistent disk. If you want to use an external PostgreSQL database, you can set the `langflow.database` values in the `values.yaml` file.
`
_30
# Deploy postgresql. You can skip this section if you have an existing postgresql database.
_30
postgresql:
_30
 enabled: true
_30
 fullnameOverride: "langflow-ide-postgresql-service"
_30
 auth:
_30
  username: "langflow"
_30
  password: "langflow-postgres"
_30
  database: "langflow-db"
_30
_30
langflow:
_30
 backend:
_30
  externalDatabase:
_30
   enabled: true
_30
   driver:
_30
    value: "postgresql"
_30
   host:
_30
    value: "langflow-ide-postgresql-service"
_30
   port:
_30
    value: "5432"
_30
   database:
_30
    value: "langflow-db"
_30
   user:
_30
    value: "langflow"
_30
   password:
_30
    valueFrom:
_30
     secretKeyRef:
_30
      key: "password"
_30
      name: "langflow-ide-postgresql-service"
_30
  sqlite:
_30
   enabled: false
`
### Scaling[​](https://docs.langflow.org/<#e1d95ba6551742aa86958dc03b26129e> "Direct link to Scaling")
You can scale the number of replicas for the LangFlow backend and frontend services by changing the `replicaCount` value in the `values.yaml` file.
`
_10
langflow:
_10
 backend:
_10
  replicaCount: 3
_10
 frontend:
_10
  replicaCount: 3
`
You can scale frontend and backend services independently.
To scale vertically (increase the resources for the pods), you can set the `resources` values in the `values.yaml` file.
`
_11
langflow:
_11
 backend:
_11
  resources:
_11
   requests:
_11
    memory: "2Gi"
_11
    cpu: "1000m"
_11
 frontend:
_11
  resources:
_11
   requests:
_11
    memory: "1Gi"
_11
    cpu: "1000m"
`
### Deploy on AWS EKS, Google GKE, or Azure AKS and other examples[​](https://docs.langflow.org/<#a8c3d4dc4e4f42f49b21189df5e2b851> "Direct link to Deploy on AWS EKS, Google GKE, or Azure AKS and other examples")
Visit the [LangFlow Helm Charts repository](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow-helm-charts>) for more information.
## LangFlow (Runtime)[​](https://docs.langflow.org/<#49f2813ad2d3460081ad26a286a65e73> "Direct link to LangFlow \(Runtime\)")
The runtime chart is tailored for deploying applications in a production environment. It is focused on stability, performance, isolation, and security to ensure that applications run reliably and efficiently.
Using a dedicated deployment for a set of flows is fundamental in production environments to have granular resource control.
### Prerequisites[​](https://docs.langflow.org/<#3ad3a9389fff483ba8bd309189426a9d> "Direct link to Prerequisites")
  * Kubernetes server
  * kubectl
  * Helm


### Step 0. Prepare a Kubernetes cluster[​](https://docs.langflow.org/<#aaa764703ec44bd5ba64b5ef4599630b> "Direct link to Step 0. Prepare a Kubernetes cluster")
Follow the same steps as for the LangFlow IDE.
### Step 1. Install the LangFlow runtime Helm chart[​](https://docs.langflow.org/<#72a18aa8349c421186ba01d73a002531> "Direct link to Step 1. Install the LangFlow runtime Helm chart")
  1. Add the repository to Helm.
`
_10
helm repo add langflow <https://langflow-ai.github.io/langflow-helm-charts>
_10
helm repo update
`
  2. Install the LangFlow app with the default options in the `langflow` namespace. If you bundled the flow in a docker image, you can specify the image name in the `values.yaml` file or with the `-set` flag: If you want to download the flow from a remote location, you can specify the URL in the `values.yaml` file or with the `-set` flag:
`
_10
helm install my-langflow-app langflow/langflow-runtime -n langflow --create-namespace --set image.repository=myuser/langflow-just-chat --set image.tag=1.0.0
`
`
_10
helm install my-langflow-app langflow/langflow-runtime -n langflow --create-namespace --set downloadFlows.flows[0].url=https://raw.githubusercontent.com/langflow-ai/langflow/dev/src/backend/base/langflow/initial_setup/starter_projects/Basic%20Prompting%20(Hello%2C%20world!).json
`
  3. Check the status of the pods.
`
_10
kubectl get pods -n langflow
`


### Step 2. Access the LangFlow app API[​](https://docs.langflow.org/<#e13326fc07734e4aa86dfb75ccfa31f8> "Direct link to Step 2. Access the LangFlow app API")
Enable local port forwarding to access LangFlow from your local machine.
`
_10
kubectl port-forward -n langflow svc/langflow-my-langflow-app 7860:7860
`
Now you can access the API at `http://localhost:7860/api/v1/flows` and execute the flow:
`
_10
id=$(curl -s <http://localhost:7860/api/v1/flows> | jq -r '.flows[0].id')
_10
curl -X POST \\
_10
  "<http://localhost:7860/api/v1/run/$id?stream=false>" \\
_10
  -H 'Content-Type: application/json'\\
_10
  -d '{
_10
   "input_value": "Hello!",
_10
   "output_type": "chat",
_10
   "input_type": "chat"
_10
  }'
`
### Storage[​](https://docs.langflow.org/<#09514d2b59064d37b685c7c0acecb861> "Direct link to Storage")
In this case, storage is not needed as our deployment is stateless.
### Log level and LangFlow configurations[​](https://docs.langflow.org/<#ecd97f0be96d4d1cabcc5b77a2d00980> "Direct link to Log level and LangFlow configurations")
You can set the log level and other LangFlow configurations in the `values.yaml` file.
`
_10
env:
_10
 - name: LANGFLOW_LOG_LEVEL
_10
  value: "INFO"
`
### Configure secrets and variables[​](https://docs.langflow.org/<#b91929e92acf47c183ea4c9ba9d19514> "Direct link to Configure secrets and variables")
To inject secrets and LangFlow global variables, you can use the `secrets` and `env` sections in the `values.yaml` file.
Let's say your flow uses a global variable which is a secret; when you export the flow as JSON, it's recommended to not include it. When importing the flow in the LangFlow runtime, you can set the global variable using the `env` section in the `values.yaml` file. Assuming you have a global variable called `openai_key_var`, you can read it directly from a secret:
`
_10
env:
_10
 - name: openai_key_var
_10
  valueFrom:
_10
   secretKeyRef:
_10
    name: openai-key
_10
    key: openai-key
`
or directly from the values file (not recommended for secret values!):
`
_10
env:
_10
 - name: openai_key_var
_10
  value: "sk-...."
`
### Scaling[​](https://docs.langflow.org/<#359b9ea5302147ebbed3ab8aa49dae8d> "Direct link to Scaling")
You can scale the number of replicas for the LangFlow app by changing the `replicaCount` value in the `values.yaml` file.
`
_10
replicaCount: 3
`
To scale vertically (increase the resources for the pods), you can set the `resources` values in the `values.yaml` file.
`
_10
resources:
_10
 requests:
_10
  memory: "2Gi"
_10
  cpu: "1000m"
`
## Other Examples[​](https://docs.langflow.org/<#8522b4276b51448e9f8f0c6efc731a7c> "Direct link to Other Examples")
Visit the LangFlow Helm Charts repository for more examples and configurations. Use the default values file as reference for all the options available.
note
Visit the examples directory to learn more about different deployment options.
[PreviousHuggingFace Spaces](https://docs.langflow.org/</deployment-hugging-face-spaces>)[NextRailway](https://docs.langflow.org/</deployment-railway>)
  * [LangFlow (IDE)](https://docs.langflow.org/<#cb60b2f34e70490faf231cb0fe1a4b42>)
    * [Prerequisites](https://docs.langflow.org/<#3efd3c63ff8849228c136f9252e504fd>)
    * [Step 0. Prepare a Kubernetes cluster](https://docs.langflow.org/<#290b9624770a4c1ba2c889d384b7ef4c>)
    * [Step 1. Install the LangFlow Helm chart](https://docs.langflow.org/<#b5c2a35144634a05a392f7e650929efe>)
    * [Step 2. Access LangFlow](https://docs.langflow.org/<#34c71d04351949deb6c8ed7ffe30eafb>)
    * [LangFlow version](https://docs.langflow.org/<#645c6ef7984d4da0bcc4170bab0ff415>)
    * [Storage](https://docs.langflow.org/<#6772c00af79147d293c821b4c6905d3b>)
    * [Scaling](https://docs.langflow.org/<#e1d95ba6551742aa86958dc03b26129e>)
    * [Deploy on AWS EKS, Google GKE, or Azure AKS and other examples](https://docs.langflow.org/<#a8c3d4dc4e4f42f49b21189df5e2b851>)
  * [LangFlow (Runtime)](https://docs.langflow.org/<#49f2813ad2d3460081ad26a286a65e73>)
    * [Prerequisites](https://docs.langflow.org/<#3ad3a9389fff483ba8bd309189426a9d>)
    * [Step 0. Prepare a Kubernetes cluster](https://docs.langflow.org/<#aaa764703ec44bd5ba64b5ef4599630b>)
    * [Step 1. Install the LangFlow runtime Helm chart](https://docs.langflow.org/<#72a18aa8349c421186ba01d73a002531>)
    * [Step 2. Access the LangFlow app API](https://docs.langflow.org/<#e13326fc07734e4aa86dfb75ccfa31f8>)
    * [Storage](https://docs.langflow.org/<#09514d2b59064d37b685c7c0acecb861>)
    * [Log level and LangFlow configurations](https://docs.langflow.org/<#ecd97f0be96d4d1cabcc5b77a2d00980>)
    * [Configure secrets and variables](https://docs.langflow.org/<#b91929e92acf47c183ea4c9ba9d19514>)
    * [Scaling](https://docs.langflow.org/<#359b9ea5302147ebbed3ab8aa49dae8d>)
  * [Other Examples](https://docs.langflow.org/<#8522b4276b51448e9f8f0c6efc731a7c>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
