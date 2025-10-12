# conftest.py
from typing import Any
import pytest

def _add_text(report, title: str, content: str):
    try:
        from pytest_html import extras
    except Exception:
        return
    extras_list = list(getattr(report, "extras", []) or [])
    extras_list.append(extras.text(content, name=title))
    report.extras = extras_list

def _add_json(report, title: str, obj: Any):
    try:
        from pytest_html import extras
    except Exception:
        return
    extras_list = list(getattr(report, "extras", []) or [])
    extras_list.append(extras.json(obj, name=title))
    report.extras = extras_list

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call":
        return
    expected_text  = getattr(item, "expected_text", None)
    expected_json  = getattr(item, "expected_json", None)
    response_json  = getattr(item, "response_json", None)
    if expected_text:
        _add_text(report, "Expected", expected_text)
    if expected_json is not None:
        _add_json(report, "Expected Response JSON", expected_json)
    if response_json is not None:
        _add_json(report, "Response JSON", response_json)
