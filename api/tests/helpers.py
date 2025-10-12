import logging

log = logging.getLogger(__name__)


def assert_status_and_attach(
    request,
    resp,
    expected_status: int,
    path: str,
    *,
    expected_json=None,
    attach_response_json: bool = True,
):

    # Expected (texto)
    request.node.expected_text = f"Expected: status={expected_status} for {path}"

    # Expected JSON
    if expected_json is not None:
        request.node.expected_json = expected_json

    # Response JSON
    if attach_response_json:
        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            try:
                request.node.response_json = resp.json()
            except Exception:
                pass

    # Log (aparece mesmo quando PASSA)
    log.info(
        "Expected %s Should be %s | Status Code %s",
        expected_status,
        path,
        resp.status_code,
    )

    # Assert do status
    assert (
        resp.status_code == expected_status
    ), f"Expected: {expected_status} Should be {path} | Status Code: {resp.status_code}"
