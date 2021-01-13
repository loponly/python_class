import pytest
from Website1 import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    print(response.data)
    assert response.data == b'Hello, World! '


def test_init_db(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('Website1.db.init_tables', fake_init_db())
    result = runner.invoke(args=['init-table'])
    assert result.output == 'Tables are created\n'
    assert Recorder.called


class AutAction(object):
    def __init__(self, client):
        self._client = client


if __name__ == "__main__":
    pytest.main(['tests/test_factory.py'])
