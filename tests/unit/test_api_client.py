import pytest
import requests
from app import api_get

class DummyResp:
    def __init__(self, ok, json_data):
        self.ok = ok
        self._json = json_data
    def raise_for_status(self):
        if not self.ok:
            raise requests.HTTPError()
    def json(self):
        return self._json

def test_api_get(monkeypatch):
    called = {}
    def fake_get(url, params):
        called['url'] = url
        return DummyResp(True, {'foo':'bar'})

    monkeypatch.setattr(requests, 'get', fake_get)
    data = api_get('/test', {'a':1})
    assert data == {'foo':'bar'}
    assert '/test' in called['url']
