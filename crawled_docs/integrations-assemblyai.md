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
    * [AssemblyAI](https://docs.langflow.org/</integrations-assemblyai>)
    * [Integrate Composio with Langflow](https://docs.langflow.org/</integrations-composio>)
    * [Langfuse](https://docs.langflow.org/</integrations-langfuse>)
    * [LangSmith](https://docs.langflow.org/</integrations-langsmith>)
    * [LangWatch](https://docs.langflow.org/</integrations-langwatch>)
    * [Google](https://docs.langflow.org/</integrations-setup-google-oauth-langflow>)
    * [Notion](https://docs.langflow.org/</integrations/notion/setup>)
  * [Contributing](https://docs.langflow.org/</contributing-community>)
  * [API reference](https://docs.langflow.org/</api-reference-api-examples>)
  * [Changelog](https://docs.langflow.org/<https:/github.com/langflow-ai/langflow/releases/latest>)


  * [](https://docs.langflow.org/</>)
  * Integrations
  * AssemblyAI


On this page
# AssemblyAI
The AssemblyAI components allow you to apply powerful Speech AI models to your app for tasks like:
  * Transcribing audio and video files
  * Formatting transcripts
  * Generating subtitles
  * Applying LLMs to audio files


More info about AssemblyAI:
  * [Website](https://docs.langflow.org/<https:/www.assemblyai.com/>)
  * [AssemblyAI API Docs](https://docs.langflow.org/<https:/www.assemblyai.com/docs>)
  * [Get a Free API key](https://docs.langflow.org/<https:/www.assemblyai.com/dashboard/signup>)


## Prerequisites[​](https://docs.langflow.org/<#prerequisites> "Direct link to Prerequisites")
You need an **AssemblyAI API key**. After creating a free account, you'll find the API key in your dashboard. [Get a Free API key here](https://docs.langflow.org/<https:/www.assemblyai.com/dashboard/signup>).
Enter the key in the _AssemblyAI API Key_ field in all components that require the key.
(Optional): To use LeMUR, you need to upgrade your AssemblyAI account, since this is not included in the free account.
## Components[​](https://docs.langflow.org/<#components> "Direct link to Components")
![AssemblyAI Components](https://docs.langflow.org/assets/images/assemblyai-components-b88c7c97e04114bf658898f7fc633e23.png)
### AssemblyAI Start Transcript[​](https://docs.langflow.org/<#assemblyai-start-transcript> "Direct link to AssemblyAI Start Transcript")
This component allows you to submit an audio or video file for transcription.
**Tip** : You can freeze the path of this component to only submit the file once.
  * **Input** :
    * AssemblyAI API Key: Your API key.
    * Audio File: The audio or video file to transcribe.
    * Speech Model (Optional): Select the class of models. Default is _Best_. See [speech models](https://docs.langflow.org/<https:/www.assemblyai.com/docs/speech-to-text/speech-recognition#select-the-speech-model-with-best-and-nano>) for more info.
    * Automatic Language Detection (Optional): Enable automatic language detection.
    * Language (Optional): The language of the audio file. Can be set manually if automatic language detection is disabled. See [supported languages](https://docs.langflow.org/<https:/www.assemblyai.com/docs/getting-started/supported-languages>) for a list of supported language codes.
    * Enable Speaker Labels (Optional): Detect speakers in an audio file and what each speaker said.
    * Expected Number of Speakers (Optional): Set the expected number of speakers, if Speaker Labels is enabled.
    * Audio File URL (Optional): The URL of the audio or video file to transcribe. Can be used instead of _Audio File_.
    * Punctuate (Optional): Apply punctuation. Default is true.
    * Format Text (Optional): Apply casing and text formatting. Default is true.
  * **Output** :
    * Transcript ID: The id of the transcript


### AssemblyAI Poll Transcript[​](https://docs.langflow.org/<#assemblyai-poll-transcript> "Direct link to AssemblyAI Poll Transcript")
This components allows you to poll the transcripts. It checks the status of the transcript every few seconds until the transcription is completed.
  * **Input** :
    * AssemblyAI API Key: Your API key.
    * Polling Interval (Optional): The polling interval in seconds. Default is 3.
  * **Output** :
    * Transcription Result: The AssemblyAI JSON response of a completed transcript. Contains the text and other info.


### AssemblyAI Get Subtitles[​](https://docs.langflow.org/<#assemblyai-get-subtitles> "Direct link to AssemblyAI Get Subtitles")
This component allows you to generate subtitles in SRT or VTT format.
  * **Input** :
    * AssemblyAI API Key: Your API key.
    * Transcription Result: The output of the _Poll Transcript_ component.
    * Subtitle Format: The format of the captions (SRT or VTT).
    * Character per Caption (Optional): The maximum number of characters per caption (0 for no limit).
  * **Output** :
    * Subtitles: A JSON response with the `subtitles` field containing the captions in SRT or VTT format.


### AssemblyAI LeMUR[​](https://docs.langflow.org/<#assemblyai-lemur> "Direct link to AssemblyAI LeMUR")
This component allows you to apply Large Language Models to spoken data using the [AssemblyAI LeMUR framework](https://docs.langflow.org/<https:/www.assemblyai.com/docs/lemur>).
LeMUR automatically ingests the transcript as additional context, making it easy to apply LLMs to audio data. You can use it for tasks like summarizing audio, extracting insights, or asking questions.
  * **Input** :
    * AssemblyAI API Key: Your API key.
    * Transcription Result: The output of the _Poll Transcript_ component.
    * Input Prompt: The text to prompt the model. You can type your prompt in this field or connect it to a _Prompt_ component.
    * Final Model: The model that is used for the final prompt after compression is performed. Default is Claude 3.5 Sonnet.
    * Temperature (Optional): The temperature to use for the model. Default is 0.0.
    * Max Output Size (Optional): Max output size in tokens, up to 4000. Default is 2000.
    * Endpoint (Optional): The LeMUR endpoint to use. Default is "task". For "summary" and "question-answer", no prompt input is needed. See [LeMUR API docs](https://docs.langflow.org/<https:/www.assemblyai.com/docs/api-reference/lemur/>) for more info.
    * Questions (Optional): Comma-separated list of your questions. Only used if _Endpoint_ is "question-answer".
    * Transcript IDs (Optional): Comma-separated list of transcript IDs. LeMUR can perform actions over multiple transcripts. If provided, the _Transcription Result_ is ignored.
  * **Output** :
    * LeMUR Response: The generated LLM response.


### AssemblyAI List Transcripts[​](https://docs.langflow.org/<#assemblyai-list-transcripts> "Direct link to AssemblyAI List Transcripts")
This component can be used as a standalone component to list all previously generated transcripts.
  * **Input** :
    * AssemblyAI API Key: Your API key.
    * Limit (Optional): Maximum number of transcripts to retrieve. Default is 20, use 0 for all.
    * Filter (Optional): Filter by transcript status.
    * Created On (Optional): Only get transcripts created on this date (YYYY-MM-DD).
    * Throttled Only (Optional): Only get throttled transcripts, overrides the status filter
  * **Output** :
    * Transcript List: A list of all transcripts with info such as the transcript ID, the status, and the data.


## Flow Process[​](https://docs.langflow.org/<#flow-process> "Direct link to Flow Process")
  1. The user inputs an audio or video file.
  2. The user can also input an LLM prompt. In this example, we want to generate a summary of the transcript.
  3. The flow submits the audio file for transcription.
  4. The flow checks the status of the transcript every few seconds until transcription is completed.
  5. The flow parses the transcription result and outputs the transcribed text.
  6. The flow also generates subtitles.
  7. The flow applies the LLM prompt to generate a summary.
  8. As a standalone component, all transcripts can be listed.


## Run the Transcription and Speech AI Flow[​](https://docs.langflow.org/<#run-the-transcription-and-speech-ai-flow> "Direct link to Run the Transcription and Speech AI Flow")
To run the Transcription and Speech AI Flow:
  1. Open Langflow and create a new project.
  2. Add the components listed above to your flow canvas, or download the [AssemblyAI Transcription and Speech AI Flow](https://docs.langflow.org/</assets/files/AssemblyAI_Flow-368be24ae9542f0b8b5253cc9d97b42f.json>)(Download link) and **Import** the JSON file into Langflow.
  3. Connect the components as shown in the flow diagram. **Tip** : Freeze the path of the _Start Transcript_ component to only submit the file once.
  4. Input the AssemblyAI API key in in all components that require the key (Start Transcript, Poll Transcript, Get Subtitles, LeMUR, List Transcripts).
  5. Select an audio or video file in the _Start Transcript_ component.
  6. Run the flow by clicking **Play** on the _Parse Data_ component. Make sure that the specified template is `{text}`.
  7. To generate subtitles, click **Play** on the _Get Subtitles_ component.
  8. To apply an LLM to your audio file, click **Play** on the _LeMUR_ component. Note that you need an upgraded AssemblyAI account to use LeMUR.
  9. To list all transcripts, click **Play** on the _List Transcript_ component.


## Customization[​](https://docs.langflow.org/<#customization> "Direct link to Customization")
The flow can be customized by:
  1. Modifying the parameters in the _Start Transcript_ component.
  2. Modifying the subtitle format in the _Get Subtitles_ component.
  3. Modifying the LLM prompt for input of the _LeMUR_ component.
  4. Modifying the LLM parameters (e.g., temperature) in the _LeMUR_ component.


## Troubleshooting[​](https://docs.langflow.org/<#troubleshooting> "Direct link to Troubleshooting")
If you encounter issues:
  1. Ensure the API key is correctly set in all components that require the key.
  2. To use LeMUR, you need to upgrade your AssemblyAI account, since this is not included in the free account.
  3. Verify that all components are properly connected in the flow.
  4. Review the Langflow logs for any error messages.


For more advanced usage, refer to the [AssemblyAI API documentation](https://docs.langflow.org/<https:/www.assemblyai.com/docs/>). If you need more help, you can reach out to the [AssemblyAI support](https://docs.langflow.org/<https:/www.assemblyai.com/contact/support>).
[PreviousRender](https://docs.langflow.org/</deployment-render>)[NextIntegrate Composio with Langflow](https://docs.langflow.org/</integrations-composio>)
  * [Prerequisites](https://docs.langflow.org/<#prerequisites>)
  * [Components](https://docs.langflow.org/<#components>)
    * [AssemblyAI Start Transcript](https://docs.langflow.org/<#assemblyai-start-transcript>)
    * [AssemblyAI Poll Transcript](https://docs.langflow.org/<#assemblyai-poll-transcript>)
    * [AssemblyAI Get Subtitles](https://docs.langflow.org/<#assemblyai-get-subtitles>)
    * [AssemblyAI LeMUR](https://docs.langflow.org/<#assemblyai-lemur>)
    * [AssemblyAI List Transcripts](https://docs.langflow.org/<#assemblyai-list-transcripts>)
  * [Flow Process](https://docs.langflow.org/<#flow-process>)
  * [Run the Transcription and Speech AI Flow](https://docs.langflow.org/<#run-the-transcription-and-speech-ai-flow>)
  * [Customization](https://docs.langflow.org/<#customization>)
  * [Troubleshooting](https://docs.langflow.org/<#troubleshooting>)


Hi, how can I help you?
![](https://docs.langflow.org/img/langflow-icon-black-transparent.svg)
