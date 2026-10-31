import pytest
import requests
from dify_plugin.errors.model import CredentialsValidateFailedError

from models._credentials import validate_model_access


class FakeResponse:
    def __init__(self, status_code=200, payload=None):
        self.status_code = status_code
        self._payload = payload

    def json(self):
        if isinstance(self._payload, Exception):
            raise self._payload
        return self._payload


def test_requires_api_key():
    with pytest.raises(CredentialsValidateFailedError, match="required"):
        validate_model_access({"api_key": " "})


def test_accepts_valid_model_list(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        lambda *args, **kwargs: FakeResponse(
            payload={"data": [{"id": "claude-sonnet-5"}]}
        ),
    )

    validate_model_access({"api_key": "sk-test"}, "claude-sonnet-5")


def test_rejects_missing_model(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        lambda *args, **kwargs: FakeResponse(
            payload={"data": [{"id": "another-model"}]}
        ),
    )

    with pytest.raises(CredentialsValidateFailedError, match="not available"):
        validate_model_access({"api_key": "sk-test"}, "claude-sonnet-5")


def test_rejects_invalid_key(monkeypatch):
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: FakeResponse(401))

    with pytest.raises(CredentialsValidateFailedError, match="Invalid"):
        validate_model_access({"api_key": "sk-test"})
