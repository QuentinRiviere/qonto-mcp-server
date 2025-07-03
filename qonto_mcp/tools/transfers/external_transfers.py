import requests
from typing import Optional, List

from requests.exceptions import RequestException
import qonto_mcp
from qonto_mcp import mcp


@mcp.tool()
def get_qonto_external_transfer(transfer_id: str):
    """
    Retrieves a specific external transfer from the Qonto API.

    Args:
        transfer_id: UUID of the external transfer to retrieve

    Example: get_qonto_external_transfer(transfer_id='7b7a5ed6-3903-4782-889d-b4f64bd7bef9')
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/external_transfers/{transfer_id}"

    try:
        response = requests.get(url, headers=qonto_mcp.headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Failed to fetch external transfer {str(e)}")


@mcp.tool()
def list_qonto_external_transfers(
    scheduled_date_from: Optional[str] = None,
    scheduled_date_to: Optional[str] = None,
    updated_at_from: Optional[str] = None,
    updated_at_to: Optional[str] = None,
    beneficiary_ids: Optional[List[str]] = None,
    page: Optional[str] = None,
    per_page: Optional[str] = None,
    sort_by: Optional[str] = None,
    status: Optional[List[str]] = None,
):
    """
    Retrieves a list of external transfers from the Qonto API with optional filtering.

    Args:
        scheduled_date_from: Filter transfers scheduled on or after this date (YYYY-MM-DD)
        scheduled_date_to: Filter transfers scheduled on or before this date (YYYY-MM-DD)
        updated_at_from: Filter transfers updated on or after this date/time (ISO 8601)
        updated_at_to: Filter transfers updated on or before this date/time (ISO 8601)
        beneficiary_ids: List of beneficiary UUIDs to filter by
        page: Page number for pagination
        per_page: Number of transfers per page
        sort_by: Sort by property and order (options: updated_at:asc, updated_at:desc,
                 scheduled_date:asc, scheduled_date:desc)
        status: List of statuses to filter by (options: pending, processing, canceled,
                declined, settled)

    Example: list_qonto_external_transfers(
                scheduled_date_from='2023-01-01',
                status=['pending', 'processing']
             )
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/external_transfers"
    params = {}

    if scheduled_date_from:
        params["scheduled_date_from"] = scheduled_date_from
    if scheduled_date_to:
        params["scheduled_date_to"] = scheduled_date_to
    if updated_at_from:
        params["updated_at_from"] = updated_at_from
    if updated_at_to:
        params["updated_at_to"] = updated_at_to
    if beneficiary_ids:
        params["beneficiary_ids[]"] = beneficiary_ids
    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page
    if sort_by:
        params["sort_by"] = sort_by
    if status:
        for st in status:
            params.setdefault("status[]", []).append(st)

    try:
        response = requests.get(url, headers=qonto_mcp.headers, params=params)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise RuntimeError(f"Failed to fetch external transfers {str(e)}")
