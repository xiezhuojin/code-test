import pytest

from code_test.app import app as _app

@pytest.fixture
def app():
    return _app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()