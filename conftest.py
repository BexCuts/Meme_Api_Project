import pytest
import requests
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
    return CreateToken(None)


@pytest.fixture
def post_endpoint(create_new_token):
    return CreateObject(create_new_token)


@pytest.fixture
def put_endpoint(create_new_token):
    return PutObject(create_new_token)


@pytest.fixture
def delete_endpoint(create_new_token):
    return DeleteObject(create_new_token)


@pytest.fixture
def get_all_endpoint(create_new_token):
    return GetObjects(create_new_token)


@pytest.fixture
def get_one_endpoint(create_new_token):
    return GetObjectById(create_new_token)


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
    headers = {'Content-type': 'application/json'}
    response = post_endpoint.create_object(body, headers)
    object_id = response.json()['id']
    yield object_id
    print('delete object')
    requests.delete(f'http://167.172.172.115:52355/{object_id}')
