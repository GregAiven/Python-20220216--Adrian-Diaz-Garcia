import asyncio
import itertools
import logging
import re
from typing import Dict

import httpx  # https://www.python-httpx.org/

from monitor.settings import WEBS


async def check_all():
    """
    Monitor all function to asynchronously run all the checks for all the webs
    defined in settings.py
    :return: dictionary with status, check_result
    :rtype:
    """
    async with httpx.AsyncClient() as async_requester:
        return await asyncio.gather(*map(check_single, WEBS, itertools.repeat(async_requester)))


async def check_single(web, async_requester) -> Dict:
    """
    Check each single website
    :param web: dictionary containing url and pattern
    :type web: dict
    :param async_requester: httpx async client
    :type async_requester: httpx.AsyncClient
    :return: dictionary containing https_status, check_result, elapsed in seconds, regex used and url
    :rtype: dict
    """

    url, re_pattern = web.get("url"), web.get("pattern")
    if not url:
        logging.warning("Found entry without url provided - %s", web)
        return {}

    logging.debug("Making request for %s and asserting regex %s", url, re_pattern)
    response = await async_requester.get(url)

    # TODO: use a proper class if required, for now a dictionary should be enough
    return {
        "http_status": response.status_code,
        "check_result": bool(re.search(re_pattern, response.text)),
        "elapsed": response.elapsed.total_seconds(),
        "regex": re_pattern,
        "url": url,
    }
