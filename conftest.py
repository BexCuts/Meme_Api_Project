import pytest
from endpoints.create_token_endpoint import CreateToken
from endpoints.post_endpoint import CreateObject
from endpoints.put_endpoint import PutObject
from endpoints.delete_endpoint import DeleteObject
from endpoints.get_all_endpoint import GetObjects
from endpoints.get_one_endpoint import GetObjectById


@pytest.fixture(scope="session")
def before_run_and_end():
    print('Start testing')
    yield
    print('Testing complete')


@pytest.fixture
def create_token_endpoint():
    return CreateToken()


@pytest.fixture
def post_endpoint():
    return CreateObject()


@pytest.fixture
def put_endpoint():
    return PutObject


@pytest.fixture
def delete_endpoint():
    return DeleteObject


@pytest.fixture
def get_all_endpoint():
    return GetObjects()


@pytest.fixture
def get_one_endpoint():
    return GetObjectById()


@pytest.fixture()
def create_new_token(create_token_endpoint):
    body = {
        "name": "SpongeBob"
    }
    headers = {'content-type': 'application/json'}
    response = create_token_endpoint.create_new_token(body, headers)
    token = response.json()['token']
    return token


@pytest.fixture()
def object_id(post_endpoint):
    body = {
        {
            "text": "some",
            "tags": [
                1,
                2,
                3
            ],
            "info": {
                "first": 1,
                "second": 2
            },
            "url": 'https://example.com'
        }
    }
    headers = {'Content-type': 'application/json'}
    response = post_endpoint.create_object(body, headers)
    object_id = response.json()['id']
    return object_id
