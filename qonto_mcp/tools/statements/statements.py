import requests
from datetime import datetime
from typing import Dict, Optional
from requests.exceptions import RequestException

import qonto_mcp
from qonto_mcp import mcp


@mcp.tool()
def get_statements(
    current_page: Optional[int] = None,
    per_page: Optional[int] = None,
    created_at_from: Optional[datetime] = None,
    created_at_to: Optional[datetime] = None,
) -> Dict:
    """
    Retrieve statements from Qonto API.

    Args:
        current_page: The current page of results to retrieve.
        per_page: The number of results per page.
        created_at_from: Filter statements created from this date.
        created_at_to: Filter statements created until this date.

    Example: get_statements(per_page=10)
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/statements"
    params = {}
    if current_page is not None:
        params["current_page"] = current_page
    if per_page is not None:
        params["per_page"] = per_page
    if created_at_from is not None:
        params["created_at_from"] = created_at_from.isoformat()
    if created_at_to is not None:
        params["created_at_to"] = created_at_to.isoformat()

    try:
        response = requests.get(url, headers=qonto_mcp.headers, params=params)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Error fetching  statements: {str(e)}")


@mcp.tool()
def download_statement(statement_id: str) -> Dict:
    """
    Download a specific statement from Qonto API.

    Args:
        statement_id: The ID of the statement to download.

    Example: download_statement(statement_id="a1b2c3d4-5678-90ab-cdef-ghijklmnopqr")
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/statements/{statement_id}/download"

    try:
        response = requests.get(url, headers=qonto_mcp.headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Error downloading  statement {str(e)}")
