from pydantic import BaseModel, Field
from dataclasses import dataclass
import pytest


class ObjectData(BaseModel):
    id: int
    text: str
    url: str
    tags: list
    info: object


TEST_POSITIVE_DATA = [
    {"text": "some", "tags": [1, 2, 3], "info": {"first": 1, "second": 2}, "url": "https://example.com"},
    {"text": "что-то", "tags": ["1", "2", "3"], "info": {1: 1, 2: 2}, "url": "some_string"},
    {"text": "#!@#!@#", "tags": ["!", 2, 10123123123], "info": {"first": 1, "second": 2}, "url": "123"}
]

TEST_NEGATIVE_DATA = [
    {"text": 1, "tags": [1, 2, 3], "info": {"first": 1, "second": 2}, "url": "https://example.com"},
    {"text": "some", "tags": {1, 2, 3}, "info": {"first": 1, "second": 2}, "url": "https://example.com"},
    {"text": "some", "tags": [1, 2, 3], "info": 321, "url": 777}
]


@pytest.mark.smoke("smoke_test")
@pytest.mark.parametrize("data", TEST_POSITIVE_DATA)
def test_create_object(create_post_endpoint, object_id, data):
    create_post_endpoint.create_object(object_id, body=data)
    create_post_endpoint.check_status_code()
    create_post_endpoint.check_response_text(data['text'])


@pytest.mark.smoke("smoke_test")
@pytest.mark.parametrize("data", TEST_NEGATIVE_DATA)
def test_update_object(put_endpoint, object_id, data):
    response = put_endpoint.update_object(object_id, data=data)
    put_endpoint.check_status_code()
    put_endpoint.check_response_text(data['text'])
    put_endpoint.check_id(data['id'])
    ObjectData(**response.json())


@pytest.mark.medium("medium")
def test_get_all_objects(get_all_endpoint):
    get_all_endpoint.get_all_objects()
    get_all_endpoint.check_status_code()


@pytest.mark.medium("medium")
def test_get_object_by_id(get_one_endpoint, object_id):
    get_one_endpoint.get_object_by_id(object_id)
    get_one_endpoint.check_status_code()
    get_one_endpoint.check_id()


@pytest.mark.smoke("smoke_test")
def test_delete_object(delete_endpoint, object_id):
    delete_endpoint.delete_object(object_id)
    delete_endpoint.check_status_code()
