<div align="center">

# 💸 Qonto Local MCP Server 🤖

</div>

<div align="center">

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-green.svg)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey.svg)
![](https://badge.mcpx.dev?type=server 'MCP Server')
![AI Powered](https://img.shields.io/badge/AI-powered-6f42c1?logo=anthropic&logoColor=white)

</div>

## 🌐 Usage

https://github.com/user-attachments/assets/619cd6a1-e064-4518-a84c-8134c09fae03

> [!IMPORTANT]
> Security and customer trust are fundamental to everything we do at Qonto. While this repository enables powerful innovation and integration capabilities, it's important to understand that certain risks are inherent to the use of the MCP technology itself. Please review the following security information carefully.


## ⚠️🔒 SECURITY NOTICE

The [MCP (Model Context Provider)](https://modelcontextprotocol.io/introduction) protocol gives AI models access to additional functionality like reading files, accessing APIs, and generate responses based on contextual data.

While this brings powerful integration capabilities, it also introduces important security considerations.

**A malicious MCP server can secretly steal credentials and maliciously exploit other trusted MCP servers you're using** ([read more](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)).

These risks are not specific to Qonto’s MCP server, but apply to any use of the MCP protocol.

We recommend to only use MCP servers you trust, just as you would with any software you install on your computer.

Questions or security concerns? Contact us at `security@qonto.com`.

## Getting started

1. Install [Claude Desktop](https://claude.ai/download)
2. Get your organization ID and API key from your Qonto account's `/settings/integrations` section:

![image](https://github.com/user-attachments/assets/2ae48bff-d393-4aaf-92e9-3170a4f324c0)

### Option 1: Docker Installation (Recommended)

#### Using Docker Compose (Easiest)

1. Clone this repository and navigate to the project directory
2. Copy the environment template:
   ```bash
   cp env.example .env
   ```
3. Edit `.env` file with your Qonto credentials:
   ```bash
   QONTO_API_KEY=your_api_key_here
   QONTO_ORGANIZATION_ID=your_organization_id_here
   QONTO_THIRDPARTY_HOST=https://thirdparty.qonto.com
   ```
4. Start the server:
   ```bash
   docker-compose up
   ```
   
   The server will be available at `http://localhost:8000` with streamable-http transport.

#### Using Docker directly

1. Build the image:
   ```bash
   docker build -t qonto-mcp-server .
   ```
2. Run with stdio transport (default):
   ```bash
   docker run --rm -i \
     -e QONTO_API_KEY=your_api_key_here \
     -e QONTO_ORGANIZATION_ID=your_organization_id_here \
     -e QONTO_THIRDPARTY_HOST=https://thirdparty.qonto.com \
     qonto-mcp-server
   ```
3. Run with streamable-http transport:
   ```bash
   docker run --rm -i \
     -e QONTO_API_KEY=your_api_key_here \
     -e QONTO_ORGANIZATION_ID=your_organization_id_here \
     -e QONTO_THIRDPARTY_HOST=https://thirdparty.qonto.com \
     -e TRANSPORT=streamable-http \
     -p 8000:8000 \
     qonto-mcp-server
   ```

#### Claude Desktop Configuration

For stdio transport, add to your `claude_desktop_config.json`:

```jsonc
{
  "mcpServers": {
    "Qonto MCP Docker": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-e", "QONTO_API_KEY=<QONTO_API_KEY>",
        "-e", "QONTO_ORGANIZATION_ID=<QONTO_ORGANIZATION_ID>",
        "-e", "QONTO_THIRDPARTY_HOST=https://thirdparty.qonto.com",
        "qonto-mcp-server"
      ]
    }
  }
}
```

For streamable-http transport:

```jsonc
{
  "mcpServers": {
    "Qonto MCP HTTP": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-e", "QONTO_API_KEY=<QONTO_API_KEY>",
        "-e", "QONTO_ORGANIZATION_ID=<QONTO_ORGANIZATION_ID>",
        "-e", "QONTO_THIRDPARTY_HOST=https://thirdparty.qonto.com",
        "-e", "TRANSPORT=streamable-http",
        "-p", "8000:8000",
        "qonto-mcp-server"
      ]
    }
  }
}
```

<details>
<summary>Option 2: Local Installation</summary>

1. Clone this repository locally
2. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/). If you're on Mac, you can just do `brew install uv`
3. In your Claude Desktop `claude_desktop_config.json` file, add the `Qonto MCP` server as follows:

> **Note**: You can optionally pass `--transport streamable-http` to use HTTP transport instead of the default `stdio` transport protocol. 

```jsonc
{
  "mcpServers": {
    "Qonto MCP": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "--with",
        "requests",
        "mcp",
        "run",
        "<PATH_TO_CLONED_REPO_FOLDER, ie. ~/development/qonto-mcp/qonto_mcp/server.py>", // <- change this
        "--transport",
        "stdio"  // <- optional: change to "streamable-http" for HTTP transport
      ],
      "env": {
        "QONTO_API_KEY": "<QONTO_API_KEY>",                 // <- change this with the API key from the settings page
        "QONTO_ORGANIZATION_ID": "<QONTO_ORGANIZATION_ID>", // <- change this with the organization id from the settings page
        "QONTO_THIRDPARTY_HOST": "https://thirdparty.qonto.com",
        "PYTHONPATH": "<PATH_TO_CLONED_REPO, ie. ~/development/qonto-mcp>" // <- change this
      }
    }
  }
}
```

For example, this is a full configuration:

```json
{
  "mcpServers": {
    "Qonto MCP": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "--with",
        "requests",
        "mcp",
        "run",
        "~/development/qonto-mcp/qonto_mcp/server.py",
        "--transport",
        "stdio"
      ],
      "env": {
        "QONTO_API_KEY": "abcdefghihlmnopqrstuvxz123456",
        "QONTO_ORGANIZATION_ID": "qonto-organization-slug-1234",
        "QONTO_THIRDPARTY_HOST": "https://thirdparty.qonto.com",
        "PYTHONPATH": "~/development/qonto-mcp"
      }
    }
  }
}
```

</details>

## Available Tools

This MCP server provides the following tools for interacting with your Qonto account:

- **Organization Info**: Get details about your Qonto organization
- **Account Management**: Access account information and balances
- **Transaction History**: Retrieve and analyze transaction data
- **Business Operations**: Access business-related financial data

## Configuration

### Environment Variables

- `QONTO_API_KEY`: Your Qonto API key (required)
- `QONTO_ORGANIZATION_ID`: Your organization ID (required)  
- `QONTO_THIRDPARTY_HOST`: API host URL (defaults to https://thirdparty.qonto.com)

### Transport Options

The server supports multiple transport protocols:

- **`stdio`** (default): Standard input/output communication, ideal for Claude Desktop integration
- **`streamable-http`**: HTTP-based communication on port 8000, useful for web applications or debugging

#### Transport Configuration

**For stdio transport:**
```bash
# Docker only
docker run -e TRANSPORT=stdio qonto-mcp-server
```

**For streamable-http transport:**
```bash
# Docker
docker run -e TRANSPORT=streamable-http -p 8000:8000 qonto-mcp-server

# Docker Compose (default)
docker-compose up
```

The server will automatically use the appropriate port and communication method based on the transport selected.

## Troubleshooting

### Common Issues

1. **Invalid API credentials**: Ensure your API key and organization ID are correct
2. **Connection timeout**: Check your network connection and API host URL
3. **Claude Desktop not recognizing the server**: Restart Claude Desktop after configuration changes

## Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
