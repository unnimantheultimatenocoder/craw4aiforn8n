[Skip to main content](https://docs.langflow.org/<#__docusaurus_skipToContent_fallback>)
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
[](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow>)[](https://docs.langflow.org/<https:/twitter.com/langflow_ai>)[](https://docs.langflow.org/<https:/discord.gg/EqksyE2EX9>)
Search...
CTRLK
[![Langflow](https://docs.langflow.org/img/langflow-logo-black.svg)](https://docs.langflow.org/</>)
  * [Welcome to Langflow](https://docs.langflow.org/</>)
  * [Get started](https://docs.langflow.org/<#>)
  * [Starter projects](https://docs.langflow.org/<#>)
  * [Tutorials](https://docs.langflow.org/<#>)
  * [Concepts](https://docs.langflow.org/<#>)
  * [Components](https://docs.langflow.org/<#>)
  * [Agents](https://docs.langflow.org/<#>)
  * [Configuration](https://docs.langflow.org/<#>)
  * [Deployment](https://docs.langflow.org/<#>)
  * [Integrations](https://docs.langflow.org/<#>)
  * [Contributing](https://docs.langflow.org/<#>)
    * [Join the Langflow community](https://docs.langflow.org/</contributing-community>)
    * [Contribute components](https://docs.langflow.org/</contributing-components>)
    * [Ask for help on the Discussions board](https://docs.langflow.org/</contributing-github-discussions>)
    * [Request an enhancement or report a bug](https://docs.langflow.org/</contributing-github-issues>)
    * [Contribute to Langflow](https://docs.langflow.org/</contributing-how-to-contribute>)
    * [Telemetry](https://docs.langflow.org/</contributing-telemetry>)
  * [API reference](https://docs.langflow.org/<#>)
  * [Changelog](https://docs.langflow.org/<#>)


  * [](https://docs.langflow.org/</>)
  * Contributing
  * Telemetry


On this page
# Telemetry
Langflow uses anonymous telemetry to collect essential usage statistics to enhance functionality and the user experience. This data helps us identify popular features and areas that need improvement, and ensures development efforts align with what you need.
We respect your privacy and are committed to protecting your data. We do not collect any personal information or sensitive data. All telemetry data is anonymized and used solely for improving Langflow.
## Opt out of telemetry[​](https://docs.langflow.org/<#opt-out-of-telemetry> "Direct link to Opt out of telemetry")
To opt out of telemetry, set the `LANGFLOW_DO_NOT_TRACK` or `DO_NOT_TRACK` environment variable to `true` before running Langflow. This disables telemetry data collection.
## Data that Langflow collects[​](https://docs.langflow.org/<#data-that-langflow-collects> "Direct link to Data that Langflow collects")
### Run[​](https://docs.langflow.org/<#2d427dca4f0148ae867997f6789e8bfb> "Direct link to Run")
  * **IsWebhook** : Indicates whether the operation was triggered via a webhook.
  * **Seconds** : Duration in seconds for how long the operation lasted, providing insights into performance.
  * **Success** : Boolean value indicating whether the operation was successful, helping identify potential errors or issues.
  * **ErrorMessage** : Provides error message details if the operation was unsuccessful, aiding in troubleshooting and enhancements.


### Shutdown[​](https://docs.langflow.org/<#081e4bd4faec430fb05b657026d1a69c> "Direct link to Shutdown")
  * **Time Running** : Total runtime before shutdown, useful for understanding application lifecycle and optimizing uptime.


### Version[​](https://docs.langflow.org/<#dc09f6aba6c64c7b8dad3d86a7cba6d6> "Direct link to Version")
  * **Version** : The specific version of Langflow used, which helps in tracking feature adoption and compatibility.
  * **Platform** : Operating system of the host machine, which aids in focusing our support for popular platforms like Windows, macOS, and Linux.
  * **Python** : The version of Python used, assisting in maintaining compatibility and support for various Python versions.
  * **Arch** : Architecture of the system (e.g., x86, ARM), which helps optimize our software for different hardware.
  * **AutoLogin** : Indicates whether the auto-login feature is enabled, reflecting user preference settings.
  * **CacheType** : Type of caching mechanism used, which impacts performance and efficiency.
  * **BackendOnly** : Boolean indicating whether you are running Langflow in a backend-only mode, useful for understanding deployment configurations.


### Playground[​](https://docs.langflow.org/<#ae6c3859f612441db3c15a7155e9f920> "Direct link to Playground")
  * **Seconds** : Duration in seconds for playground execution, offering insights into performance during testing or experimental stages.
  * **ComponentCount** : Number of components used in the playground, which helps understand complexity and usage patterns.
  * **Success** : Success status of the playground operation, aiding in identifying the stability of experimental features.


### Component[​](https://docs.langflow.org/<#630728d6654c40a6b8901459a4bc3a4e> "Direct link to Component")
  * **Name** : Identifies the component, providing data on which components are most utilized or prone to issues.
  * **Seconds** : Time taken by the component to execute, offering performance metrics.
  * **Success** : Whether the component operated successfully, which helps in quality control.
  * **ErrorMessage** : Details of any errors encountered, crucial for debugging and improvement.


[PreviousContribute to Langflow](https://docs.langflow.org/</contributing-how-to-contribute>)[NextAPI examples](https://docs.langflow.org/</api-reference-api-examples>)
  * [Opt out of telemetry](https://docs.langflow.org/<#opt-out-of-telemetry>)
  * [Data that Langflow collects](https://docs.langflow.org/<#data-that-langflow-collects>)
    * [Run](https://docs.langflow.org/<#2d427dca4f0148ae867997f6789e8bfb>)
    * [Shutdown](https://docs.langflow.org/<#081e4bd4faec430fb05b657026d1a69c>)
    * [Version](https://docs.langflow.org/<#dc09f6aba6c64c7b8dad3d86a7cba6d6>)
    * [Playground](https://docs.langflow.org/<#ae6c3859f612441db3c15a7155e9f920>)
    * [Component](https://docs.langflow.org/<#630728d6654c40a6b8901459a4bc3a4e>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
