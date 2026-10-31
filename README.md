# JZSTOKEN for Dify

JZSTOKEN provides one OpenAI-compatible API key for text models from OpenAI,
Anthropic, DeepSeek, Qwen, Zhipu, Moonshot, xAI, and other model families.

## Setup

1. Create an API key at [JZSTOKEN API Keys](https://jzstoken.com/dashboard/keys).
2. Install this plugin in Dify.
3. Open **Settings > Model Provider > JZSTOKEN**.
4. Paste the key and save. The plugin validates it with
   `GET https://jzstoken.com/api/v1/models`.

The fixed API base URL is `https://jzstoken.com/api/v1`. A Standard key can
access every model except `jzs-max-3.0`; a dedicated `jzs-max-3.0` key is
limited to that model.

## Included models

- `claude-sonnet-5`
- `claude-opus-5`
- `gpt-5.6-terra`
- `deepseek-v4-pro`
- `qwen3.8-max`

These are convenience entries, not a complete catalog. Use the customizable
model option for another model ID shown in the
[JZSTOKEN model catalog](https://jzstoken.com/model-pricing).

## Usage

Select JZSTOKEN and one of the included models in a Chatflow, Workflow, or Agent
node. For custom models, provide the exact model ID, context size, and supported
capabilities in the model configuration.

The plugin sends Chat Completions requests to JZSTOKEN. Streaming, tool calling,
vision, and structured output depend on the selected upstream model. JZSTOKEN
does not currently publish per-model certification for every optional
capability, so verify account-specific behavior before relying on it in
production.

## Limitations

- Only Chat Completions is supported by this plugin.
- The Anthropic Messages endpoint is not used by this plugin.
- Maximum output token limits are not published per model. The included model
  entries use a conservative 8192-token selector limit.
- This package was validated locally with mocked request tests. It was not
  tested against a live Dify Cloud workspace because no test workspace or API
  key was available in the development environment.

## Source repository

https://github.com/Jzstoken-bit/jzstoken-dify-plugin

## Contact

Open an issue at
https://github.com/Jzstoken-bit/jzstoken-dify-plugin/issues.

## Privacy

See [PRIVACY.md](PRIVACY.md).

## License

MIT
