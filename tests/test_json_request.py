import requests
import functools


def get_json(url):
    return requests.get(url).json()


class MockResponse:

    @staticmethod
    def json():
        return {'mock_key': 'mock_response'}


def test_get_json(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

    result = get_json('"https://fakeurl')
    assert result['mock_key'] == 'mock_response'


def test_partial(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(functools, 'partial', 3)
        assert functools.partial == 3
