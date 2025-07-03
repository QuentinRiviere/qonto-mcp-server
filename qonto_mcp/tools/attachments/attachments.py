import requests
from requests.exceptions import RequestException
import qonto_mcp
from qonto_mcp import mcp


@mcp.tool()
def get_qonto_attachment(attachment_id: str):
    """
    Retrieves an attachment's information from the Qonto API.

    Note: The download URL returned is only valid for 30 minutes. If you need to access
    the file after that time, you'll need to call this function again.

    Args:
        attachment_id: UUID of the attachment to retrieve

    Example: get_qonto_attachment(attachment_id='71c32755-d0c3-4d82-9a78-774caa9d8556')
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/attachments/{attachment_id}"

    try:
        response = requests.get(url, headers=qonto_mcp.headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Failed to fetch attachment {str(e)}")
