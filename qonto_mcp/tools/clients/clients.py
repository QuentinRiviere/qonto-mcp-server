import requests
from typing import Dict, Optional
from requests.exceptions import RequestException

import qonto_mcp
from qonto_mcp import mcp


@mcp.tool()
def get_clients(
    current_page: Optional[int] = None,
    per_page: Optional[int] = None,
) -> Dict:
    """
    Get all clients from Qonto API.

    Args:
        current_page: The current page of results to retrieve.
        per_page: The number of results per page.

    Example: get_clients(per_page=20)
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/clients"
    params = {}
    if current_page is not None:
        params["current_page"] = current_page
    if per_page is not None:
        params["per_page"] = per_page

    try:
        response = requests.get(url, headers=qonto_mcp.headers, params=params)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Error fetching clients: {str(e)}")


@mcp.tool()
def get_client(client_id: str) -> Dict:
    """
    Get a specific client from Qonto API.

    Args:
        client_id: The ID of the client to retrieve.

    Example: get_client(client_id="a1b2c3d4-5678-90ab-cdef-ghijklmnopqr")
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/clients/{client_id}"

    try:
        response = requests.get(url, headers=qonto_mcp.headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Error getting client: {str(e)}")
