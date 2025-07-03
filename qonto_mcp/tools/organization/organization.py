import requests
from requests.exceptions import RequestException
import qonto_mcp
from qonto_mcp import mcp


@mcp.tool()
def get_qonto_organization():
    """
    Retrieves organization and list of bank accounts from the Qonto API

    Example: get_qonto_organization()
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/organization"

    try:
        response = requests.get(url, headers=qonto_mcp.headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Error fetching Qonto transactions {str(e)}")
