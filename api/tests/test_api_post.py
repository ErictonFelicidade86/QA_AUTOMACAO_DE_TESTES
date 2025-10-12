import pytest
from src.client import post
from src.testdata import make_valid_post, INVALID_PAYLOADS
from tests.schemas import PostResponse
from tests.helpers import assert_status_and_attach


def _assert_has_id(json_obj):
    assert "id" in json_obj and isinstance(json_obj["id"], int) and json_obj["id"] > 0


# -----------------------------
# POST /posts - cenário "feliz"
# -----------------------------
def test_create_post_happy(request):
    path = "/posts"
    expected = 201
    payload = make_valid_post()

    resp = post(path, json=payload)
    assert_status_and_attach(request, resp, expected, path, expected_json=payload)
    data = resp.json()

    parsed = PostResponse(**data)
    assert parsed.title == payload["title"]
    assert parsed.body == payload["body"]
    assert parsed.userId == payload["userId"]
    _assert_has_id(data)


# ----------------------------------------
# POST /posts - negativos (comportamento)
# ----------------------------------------
def test_post_invalid_route(request):
    path = "/postsss"  # rota inválida
    expected = 404
    resp = post(path, json={"title": "x"})
    assert_status_and_attach(request, resp, expected, path, attach_response_json=False)


def test_post_empty_object(request):
    path = "/posts"
    expected = 404
    resp = post(path, json={})
    assert_status_and_attach(request, resp, expected, path)
    _assert_has_id(resp.json())


def test_post_without_body(request):
    path = "/posts"
    expected = 404
    resp = post(path, json=None)
    assert_status_and_attach(request, resp, expected, path)
    _assert_has_id(resp.json())


def test_post_partial_body(request):
    path = "/posts"
    expected = 404
    payload = {"title": "apenas título"}
    resp = post(path, json=payload)
    assert_status_and_attach(request, resp, expected, path, expected_json=payload)
    data = resp.json()
    _assert_has_id(data)
    if "title" in data:
        assert data["title"] == payload["title"]


@pytest.mark.parametrize("payload", INVALID_PAYLOADS)
def test_post_invalid_payloads_still_return_id(payload, request):
    path = "/posts"
    expected = 404
    resp = post(path, json=payload)
    assert_status_and_attach(request, resp, expected, path, expected_json=payload)
    _assert_has_id(resp.json())
