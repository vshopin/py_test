import requests
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.post import POST_SCHEMA
from src.base_classes.response import Response


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(400).validate(POST_SCHEMA)

# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
