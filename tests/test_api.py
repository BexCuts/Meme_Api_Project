from pydantic import BaseModel
import pytest
from conftest import meme_id


class MemeData(BaseModel):
    id: int
    text: str
    url: str
    tags: list
    info: object


body_positive = [
    {"text": "some", "tags": [1, 2, 3], "info": {"first": 1, "second": 2}, "url": "https://example.com"},
    {"text": "что-то", "tags": ["1", "2", "3"], "info": {1: 1, 2: 2}, "url": "some_string"},
    {"text": "#!@#!@#", "tags": ["!", 2, 10123123123], "info": {"first": 1, "second": 2}, "url": "123"}
]

body_negative = [
    {"text": 1, "tags": [1, 2, 3], "info": {"first": 1, "second": 2}, "url": "https://example.com"},
    {"text": "some", "tags": {1, 2, 3}, "info": {"first": 1, "second": 2}, "url": "https://example.com"},
    {"text": "some", "tags": [1, 2, 3], "info": 321, "url": 777}
]


body_for_update = [
    {"id": int, "text": "1", "tags": [1, 2, 3], "info": {"first": 1, "second": 2}, "url": "https://example.com"},
    {"id": int, "text": "22", "tags": [1, 2, 3], "info": {"first": 1, "second": 2}, "url": "https://examples.com"}
]


@pytest.mark.smoke('smoke_test')
@pytest.mark.parametrize('body', body_positive)
def test_create_meme(post_endpoint, body, auth_token):
    token, user = auth_token
    post_endpoint.create_meme(body=body, headers={'Authorization': f'{token}'})
    post_endpoint.check_response_code()
    post_endpoint.check_response_id(post_endpoint.response.json()['id'])
    MemeData(**post_endpoint.response.json())


@pytest.mark.smoke('smoke_test')
@pytest.mark.parametrize('body', body_negative)
def test_create_meme_400(post_endpoint, body, auth_token):
    token, user = auth_token
    post_endpoint.create_meme(body=body, headers={'Authorization': f'{token}'})
    post_endpoint.check_response_400_code()


@pytest.mark.smoke('smoke_test')
def test_get_all_memes(get_all_meme_endpoint, auth_token):
    token, user = auth_token
    get_all_meme_endpoint.get_all_memes(headers={'Authorization': f'{token}'})
    get_all_meme_endpoint.check_response_code()


@pytest.mark.smoke('smoke_test')
def test_get_meme_by_id(get_meme_endpoint, auth_token, meme_id):
    token, user = auth_token
    get_meme_endpoint.get_one_endpoint(meme_id=meme_id, headers={'Authorization': f'{token}'})
    get_meme_endpoint.check_response_code()
    get_meme_endpoint.check_response_id(get_meme_endpoint.response.json()['id'])


@pytest.mark.parametrize('body', body_for_update)
def test_update_meme(put_endpoint, body, meme_id, auth_token):
    token, user = auth_token
    body["id"] = int(meme_id)
    put_endpoint.update_meme(meme_id=meme_id, body=body, headers={'Authorization': f'{token}'})
    put_endpoint.check_response_code()
    put_endpoint.check_response_id(put_endpoint.response.json()['id'])
    MemeData(**put_endpoint.response.json())


# @pytest.mark.smoke
# def test_delete_meme(delete_meme_endpoint, auth_token, meme_id):
#     token, user = auth_token
#     delete_meme_endpoint.delete_meme(meme_id=meme_id, headers={'Authorization': f'{token}'})
#     delete_meme_endpoint.check_response_code()
