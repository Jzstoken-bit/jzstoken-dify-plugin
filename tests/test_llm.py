from models.llm.llm import JzstokenLargeLanguageModel


def test_model_credentials_fix_endpoint_to_jzstoken():
    model = JzstokenLargeLanguageModel([])

    credentials = model._model_credentials(
        "gpt-5.6-terra", {"api_key": "sk-test", "function_calling_type": "no_call"}
    )

    assert credentials["endpoint_url"] == "https://jzstoken.com/api/v1"
    assert credentials["mode"] == "chat"
    assert credentials["function_calling_type"] == "no_call"
    assert credentials["stream_function_calling"] == "supported"


def test_model_credentials_default_to_tool_calls():
    model = JzstokenLargeLanguageModel([])

    credentials = model._model_credentials("claude-sonnet-5", {"api_key": "sk-test"})

    assert credentials["function_calling_type"] == "tool_call"
