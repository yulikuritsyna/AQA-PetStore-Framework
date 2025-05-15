import pytest

from main.common.request import Request


@pytest.fixture
def http():
    return Request(url='https://petstore.swagger.io/v2')


@pytest.fixture
def create_body():
    return {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }


@pytest.fixture
def assert_status_code():
    def check(resp):
        assert resp.status_code == 200
    return check