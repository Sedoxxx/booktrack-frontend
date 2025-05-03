import streamlit as st
from app.pages.details import details_page
from app.api_client import api_get
import pytest

def test_details_error(monkeypatch):
    monkeypatch.setattr(api_get.__module__, 'api_get', lambda p: None)
    st.session_state['selected_book'] = 1
    # Should not raise
    details_page()
