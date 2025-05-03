import streamlit as st
from app.pages.search import search_page
from app.api_client import api_get
import pytest

def test_search_calls_api(monkeypatch):
    called = {}
    def fake_get(path, params):
        called['path'] = path
        return {'results': [], 'total_pages': 1}

    monkeypatch.setattr(api_get.__module__, 'api_get', fake_get)
    # Reset session state
    st.session_state.clear()
    search_page()
    assert called['path'] == '/books/'
