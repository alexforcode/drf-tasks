import pytest

from core.test.api_client import DRFClient


@pytest.fixture
def admin():
    return DRFClient(admin=True)


@pytest.fixture
def client():
    return DRFClient()


@pytest.fixture
def anon():
    return DRFClient(anon=True)
