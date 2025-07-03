import requests
from datetime import datetime
from typing import Dict, Optional
from requests.exceptions import RequestException

import qonto_mcp
from qonto_mcp import mcp


@mcp.tool()
def get_requests(
    current_page: Optional[int] = None,
    per_page: Optional[int] = None,
    status: Optional[str] = None,
    updated_at_from: Optional[datetime] = None,
    updated_at_to: Optional[datetime] = None,
) -> Dict:
    """
    Get requests from Qonto API.

    Args:
        current_page: The current page of results to retrieve.
        per_page: The number of results per page.
        status: Filter requests by status.
        updated_at_from: Filter requests updated from this date.
        updated_at_to: Filter requests updated until this date.

    Example: get_requests(per_page=10, status="pending")
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/requests"
    params = {}
    if current_page is not None:
        params["current_page"] = current_page
    if per_page is not None:
        params["per_page"] = per_page
    if status is not None:
        params["status"] = status
    if updated_at_from is not None:
        params["updated_at_from"] = updated_at_from.isoformat()
    if updated_at_to is not None:
        params["updated_at_to"] = updated_at_to.isoformat()

    try:
        response = requests.get(url, headers=qonto_mcp.headers, params=params)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Error fetching requests: {str(e)}")


@mcp.tool()
def get_request(request_id: str) -> Dict:
    """
    Get a specific request from Qonto API.

    Args:
        request_id: The ID of the request to retrieve.

    Example: get_request(request_id="a1b2c3d4-5678-90ab-cdef-ghijklmnopqr")
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/requests/{request_id}"

    try:
        response = requests.get(url, headers=qonto_mcp.headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Error fetching request: {str(e)}")
