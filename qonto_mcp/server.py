from dotenv import load_dotenv
import argparse
import logging
import qonto_mcp
from qonto_mcp import mcp

# Side-effect imports (tool registrations)
import qonto_mcp.tools.organization
import qonto_mcp.tools.transactions
import qonto_mcp.tools.transfers
import qonto_mcp.tools.beneficiaries
import qonto_mcp.tools.attachments
import qonto_mcp.tools.labels
import qonto_mcp.tools.memberships
import qonto_mcp.tools.invoices
import qonto_mcp.tools.statements
import qonto_mcp.tools.clients
import qonto_mcp.tools.requests

# Load environment variables
load_dotenv()

# Setup Qonto API configuration
qonto_mcp.setup_qonto_config()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # --- argument parsing ---------------------------------------------------
    parser = argparse.ArgumentParser(
        description="Run the MCP server with a selectable transport."
    )
    parser.add_argument(
        "--transport",
        choices=["streamable-http", "stdio"],
        default="stdio",
        help="Communication transport to use (default: stdio)",
    )
    args = parser.parse_args()
    # ------------------------------------------------------------------------
    # Display security notice
    logger.info("⚠️🔒 SECURITY NOTICE")
    logger.info(
        "The MCP (Model Context Provider) protocol gives AI models access to additional functionality."
    )
    logger.info(
        "While this brings powerful integration capabilities, it also introduces important security considerations."
    )
    logger.info(
        "A malicious MCP server can secretly steal credentials and maliciously exploit other trusted MCP servers."
    )
    logger.info(
        "We recommend to only use MCP servers you trust, just as you would with any software you install."
    )
    logger.info("Find out more details in the `README.md` of this repository.")

    mcp.run(transport=args.transport)
