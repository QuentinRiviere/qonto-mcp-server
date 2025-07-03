import requests
from typing import Optional, List
import qonto_mcp
from qonto_mcp import mcp


@mcp.tool()
def get_qonto_transactions(bank_account_id: str):
    """
    Retrieves transactions from the Qonto API for a specific bank account.

    Example: get_qonto_transactions(bank_account_id='0193f298-d9f3-7b77-8566-ce356449d7f3')
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/transactions"
    params = {"bank_account_id": bank_account_id}

    try:
        response = requests.get(url, headers=qonto_mcp.headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return f"Error fetching Qonto transactions: {str(e)}"


@mcp.tool()
def get_qonto_transaction(transaction_id: str, includes: list = None):
    """
    Retrieves a specific transaction from the Qonto API with optional related resources.
    
    This returns detailed information about a transaction including amounts, dates,
    counterparty details, and operation type.

    Args:
        transaction_id: UUID of the transaction to retrieve
        includes: Optional list of related resources to include. Valid options are:
                 'vat_details', 'labels', 'attachments'

    Example: get_qonto_transaction(
                transaction_id='7b7a5ed6-3903-4782-889d-b4f64bd7bef9', 
                includes=['labels', 'attachments']
             )
    """
    url = f"{qonto_mcp.thirdparty_host}/v2/transactions/{transaction_id}"
    params = {}
    
    if includes:
        for include in includes:
            params.setdefault("includes[]", []).append(include)

    try:
        response = requests.get(url, headers=qonto_mcp.headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return f"Error fetching transaction: {str(e)}"