import pytest
import requests
from endpoints.delete_endpoint import DeleteMeme
from endpoints.get_one_endpoint import GetOneMeme
from endpoints.get_all_endpoint import GetAllMemes
from endpoints.put_endpoint import UpdateEndpoint
from endpoints.post_endpoint import PostEndpoint
from endpoints.create_token_endpoint import CreateTokenEndpoint


@pytest.fixture(scope='session')
def before_and_end():
    print('Start testing')
    yield
    print('End testing')


@pytest.fixture()
def create_token():
    return CreateTokenEndpoint(None)


@pytest.fixture()
def post_endpoint(create_token):
    return PostEndpoint(create_token)


@pytest.fixture()
def put_endpoint(create_token):
    return UpdateEndpoint(create_token)


@pytest.fixture()
def get_all_meme_endpoint(create_token):
    return GetAllMemes(create_token)


@pytest.fixture()
def get_meme_endpoint(create_token):
    return GetOneMeme(create_token)


@pytest.fixture()
def delete_meme_endpoint(create_token):
    return DeleteMeme(create_token)


@pytest.fixture()
def auth_token(create_token):
    body = {
        "name": "Test"
    }
    response = requests.post('http://167.172.172.115:52355/authorize', json=body)
    token = response.json()['token']
    user = response.json()['user']
    print(token)
    return token, user


@pytest.fixture()
def check_auth_token(auth_token):
    token, user = auth_token
    response = requests.get(f'http://167.172.172.115:52355/authorize/{token}')
    print(response.json())
    if response.text == f'Token is alive. Username is {user}':
        print('Token is alive')
    else:
        print('Token is not alive')


@pytest.fixture()
def meme_id(auth_token, post_endpoint):
    token, user = auth_token
    body = {
        "text": "some_text",
        "url": "example.com",
        "tags": [
            1,
            2,
            3
        ],
        "info": {
            "one": 1,
            "two": 2
        }
    }
    headers = {'Authorization': f'{token}'}
    response = requests.post('http://167.172.172.115:52355/meme', json=body, headers=headers)
    id_meme = response.json()['id']
    yield id_meme
    print('delete meme')
    requests.delete(f'http://167.172.172.115:52355/{id_meme}')
