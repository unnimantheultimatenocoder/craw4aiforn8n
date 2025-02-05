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
  * [Integrations](https://docs.langflow.org/</integrations-assemblyai>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
    * [Join the Langflow community](https://docs.langflow.org/</contributing-community>)
    * [Contribute components](https://docs.langflow.org/</contributing-components>)
    * [Ask for help on the Discussions board](https://docs.langflow.org/</contributing-github-discussions>)
    * [Request an enhancement or report a bug](https://docs.langflow.org/</contributing-github-issues>)
    * [Contribute to Langflow](https://docs.langflow.org/</contributing-how-to-contribute>)
    * [Telemetry](https://docs.langflow.org/</contributing-telemetry>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Contributing
  * Contribute components


On this page
# Contribute components
New components are added as objects of the [CustomComponent](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/dev/src/backend/base/langflow/custom/custom_component/custom_component.py>) class.
Any dependencies are added to the [pyproject.toml](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/pyproject.toml#L148>) file.
### Contribute an example component to Langflow[​](https://docs.langflow.org/<#contribute-an-example-component-to-langflow> "Direct link to Contribute an example component to Langflow")
Anyone can contribute an example component. For example, if you created a new document loader called **MyCustomDocumentLoader** , you can follow these steps to contribute it to Langflow.
  1. Write your loader as an object of the [CustomComponent](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/dev/src/backend/base/langflow/custom/custom_component/custom_component.py>) class. You'll create a new class, `MyCustomDocumentLoader`, that will inherit from `CustomComponent` and override the base class's methods.
  2. Define optional attributes like `display_name`, `description`, and `documentation` to provide information about your custom component.
  3. Implement the `build_config` method to define the configuration options for your custom component.
  4. Implement the `build` method to define the logic for taking input parameters specified in the `build_config` method and returning the desired output.
  5. Add the code to the [/components/documentloaders](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/tree/dev/src/backend/base/langflow/components>) folder.
  6. Add the dependency to [/documentloaders/**init**.py](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/dev/src/backend/base/langflow/components/documentloaders/__init__.py>) as `from .MyCustomDocumentLoader import MyCustomDocumentLoader`.
  7. Add any new dependencies to the [pyproject.toml](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/pyproject.toml#L148>) file.
  8. Submit documentation for your component. For this example, you'd submit documentation to the [loaders page](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/blob/main/docs/docs/Components/components-loaders.md>).
  9. Submit your changes as a pull request. The Langflow team will have a look, suggest changes, and add your component to Langflow.


[PreviousJoin the Langflow community](https://docs.langflow.org/</contributing-community>)[NextAsk for help on the Discussions board](https://docs.langflow.org/</contributing-github-discussions>)
  * [Contribute an example component to Langflow](https://docs.langflow.org/<#contribute-an-example-component-to-langflow>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
