import pytest
from src.client import get
from src.testdata import VALID_POST_IDS, INVALID_IDS, INVALID_ROUTES
from tests.helpers import assert_status_and_attach


def test_get_all(request):
    path = "/posts"
    expected = 200
    resp = get(path)
    assert_status_and_attach(request, resp, expected, path)


@pytest.mark.parametrize(
    "post_id", VALID_POST_IDS, ids=[f"id_{i}" for i in VALID_POST_IDS]
)
def test_get_by_valid_ids(post_id, request):
    path = f"/posts/{post_id}"
    expected = 200
    resp = get(path)
    assert_status_and_attach(request, resp, expected, path)
    data = resp.json()
    request.node.expected_json = {"id": int(post_id)}
    assert data.get("id") == int(post_id)
    assert "title" in data and "body" in data


@pytest.mark.parametrize(
    "post_id",
    INVALID_IDS,
    ids=["inexistente", "zero", "negativo", "string", "null_literal"],
)
def test_get_invalid_ids(post_id, request):
    path = f"/posts/{post_id}"
    expected = 404
    resp = get(path)
    assert_status_and_attach(request, resp, expected, path)


@pytest.mark.parametrize(
    "path", INVALID_ROUTES, ids=["rota_errada_1", "rota_errada_2", "caractere_especial"]
)
def test_get_invalid_routes(path, request):
    expected = 404
    resp = get(path)
    assert_status_and_attach(request, resp, expected, path)
