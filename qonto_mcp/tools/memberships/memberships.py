from typing import Optional
import requests
from requests.exceptions import RequestException
import qonto_mcp
from qonto_mcp import mcp


@mcp.tool()
def list_qonto_memberships(page: Optional[str] = None, per_page: Optional[str] = None):
    """
    Retrieves all memberships for the authenticated organization from the Qonto API.

    A membership represents a user who has access to the Qonto account. The API returns
    information about each member including their role and personal details.

    Args:
        page: Page number for pagination
        per_page: Number of memberships per page

    Example: list_qonto_memberships(per_page='50')
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/memberships"
    params = {}

    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page

    try:
        response = requests.get(url, headers=qonto_mcp.headers, params=params)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Failed to fetch memberships {str(e)}")
