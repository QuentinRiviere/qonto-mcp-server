import requests
from typing import Optional, List
import qonto_mcp
from qonto_mcp import mcp


@mcp.tool()
def list_qonto_beneficiaries(
    ibans: Optional[List[str]] = None,
    status: Optional[List[str]] = None,
    trusted: Optional[bool] = None,
    updated_at_from: Optional[str] = None,
    updated_at_to: Optional[str] = None,
    page: Optional[str] = None,
    per_page: Optional[str] = None,
    sort_by: Optional[str] = None,
):
    """
    Retrieves a list of beneficiaries from the Qonto API with optional filtering.

    Args:
        ibans: List of IBANs to filter by
        status: List of statuses to filter by (options: pending, validated, declined)
        trusted: Filter by trusted state (True/False)
        updated_at_from: Filter beneficiaries updated on or after this date/time (ISO 8601)
        updated_at_to: Filter beneficiaries updated on or before this date/time (ISO 8601)
        page: Page number for pagination
        per_page: Number of beneficiaries per page
        sort_by: Sort by property and order (options: updated_at:desc, updated_at:asc)

    Example: list_qonto_beneficiaries(
                status=['validated'], 
                trusted=True
             )
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/beneficiaries"
    params = {}

    if ibans:
        for iban in ibans:
            params.setdefault("iban[]", []).append(iban)
    if status:
        for st in status:
            params.setdefault("status[]", []).append(st)
    if trusted is not None:
        params["trusted"] = trusted
    if updated_at_from:
        params["updated_at_from"] = updated_at_from
    if updated_at_to:
        params["updated_at_to"] = updated_at_to
    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page
    if sort_by:
        params["sort_by"] = sort_by

    try:
        response = requests.get(url, headers=qonto_mcp.headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return f"Error fetching beneficiaries: {str(e)}"


@mcp.tool()
def get_qonto_beneficiary(beneficiary_id: str):
    """
    Retrieves a specific beneficiary from the Qonto API.

    Args:
        beneficiary_id: UUID of the beneficiary to retrieve

    Example: get_qonto_beneficiary(beneficiary_id='e72f6e43-0f27-4415-8781-ad648a89b47f')
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/beneficiaries/{beneficiary_id}"

    try:
        response = requests.get(url, headers=qonto_mcp.headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return f"Error fetching beneficiary: {str(e)}"

