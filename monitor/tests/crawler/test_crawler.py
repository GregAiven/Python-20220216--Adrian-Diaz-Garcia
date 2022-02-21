import httpx
import pytest

import monitor.crawler
from monitor.crawler import check_all, check_single


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("url", "pattern", "http_status", "text", "check_result"),
    [
        ("https://fakeurl", "fake", 200, "This is a fake html response", True),
        ("https://fakeurl2", "non_present", 200, "This is a fake html response", False),
        ("https://fakeurl3", "fake", 500, "Server Error", False),
        ("https://notfound", "fake", 404, "Not found", False),
    ],
)
async def test_check_single(url, pattern, http_status, text, check_result, httpx_mock):
    """
    Test the differente use cases for check_single function
    This is expecting also to recieve different results for http status, content and
    check_result after looking for the provided regex.
    """
    httpx_mock.add_response(url=url, text=text, status_code=http_status)

    async with httpx.AsyncClient() as client:
        response = await check_single({"url": url, "pattern": pattern}, client)

    assert response["http_status"] == http_status
    assert response["check_result"] == check_result
    assert response["elapsed"] > 0
    assert response["regex"] == pattern
    assert response["url"] == url


@pytest.mark.asyncio
async def test_check_single_no_url():
    async with httpx.AsyncClient() as client:
        response = await check_single({"pattern": "fake"}, client)

    assert response == {}


@pytest.mark.asyncio
async def test_check_all(httpx_mock):
    """
    Test to asses that function check_all asynchronously call all the webs
    defined in the settings (in this case mockey_patched) and return the results
    """

    # Monkeypatch WEBS list used in the crawler
    monitor.crawler.WEBS = [
        {"url": "https://fakeurl", "pattern": r"fake"},
        {"url": "https://fakeurl2", "pattern": r"look"},
    ]
    httpx_mock.add_response(url="https://fakeurl", text="This is a fake text", status_code=200)
    httpx_mock.add_response(url="https://fakeurl2", text="This is a fake text", status_code=200)

    results = await check_all()

    assert results[0]["http_status"] == 200
    assert results[0]["check_result"] is True
    assert results[0]["elapsed"] > 0
    assert results[0]["regex"] == "fake"
    assert results[0]["url"] == "https://fakeurl"

    assert results[1]["http_status"] == 200
    assert results[1]["check_result"] is False
    assert results[1]["elapsed"] > 0
    assert results[1]["regex"] == "look"
    assert results[1]["url"] == "https://fakeurl2"
