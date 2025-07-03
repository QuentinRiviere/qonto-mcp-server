from typing import Optional
import requests
from requests.exceptions import RequestException
import qonto_mcp
from qonto_mcp import mcp


@mcp.tool()
def list_qonto_labels(page: Optional[str] = None, per_page: Optional[str] = None):
    """
    Retrieves all labels for the authenticated organization from the Qonto API.

    Labels can be used to categorize transactions. The API returns label hierarchy
    information (parent-child relationships).

    Args:
        page: Page number for pagination
        per_page: Number of labels per page

    Example: list_qonto_labels(per_page='50')
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/labels"
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
        raise RuntimeError(f"Error fetching labels: {str(e)}")


@mcp.tool()
def get_qonto_label(label_id: str):
    """
    Retrieves a specific label from the Qonto API.

    Labels are used to categorize transactions. The API returns information about the label
    including its name and parent label (if any).

    Args:
        label_id: UUID of the label to retrieve

    Example: get_qonto_label(label_id='2d9663fd-1748-4ed4-a590-48066ae9e1cb')
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/labels/{label_id}"

    try:
        response = requests.get(url, headers=qonto_mcp.headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Failed to fetch label {str(e)}")
