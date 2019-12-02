import pytest
from app import app

@pytest.fixture
def client():
    micro_service = app.app()
    micro_service.debug = True
    client = micro_service.test_client()
    ctx = micro_service.app_context()
    ctx.push()
    yield client
    ctx.pop()

def test_index(client):
    valid_field = 'input'
    value = 'This is content'
    client.get("/").status_code == 200

def test_invalid_field(client):
    invalid_field = 'inputs'
    value = 'This is content'

def test_missing_field(client):
    valid_field = ''
    value = ''

def test_missing_value(client):
    valid_field = 'input'
    value = ''