# import asyncio
# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from mcp_use import MCPAgent, MCPClient

# async def main():
#     # Load environment variables
#     load_dotenv()
#     os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

#     config = "/Users/dannieai/Documents/mcp_demo/.vscode/mcp.json"

#     client = MCPClient.from_config_file(config)

#     # Create LLM
#     llm = ChatGroq(model="qwen/qwen3.6-27b")

#     # Create agent with the client
#     agent = MCPAgent(llm=llm, client=client, max_steps=15, memory_enabled=True)

#     print(">>>>>>>Interactive MCP chat agentic workflow. Type 'exit' to quit.<<<<<<<")

#     # Run the query
#     result = await agent.run(
#          "Search for a nice place to stay in Barcelona on Airbnb, "
#         "then use Google to find nearby restaurants and attractions.")
    
#     print(f"\nResult: {result}")

#     await client.close_all_sessions()

# if __name__ == "__main__":
#     asyncio.run(main())

"""
Basic usage example for mcp_use.

This example demonstrates how to use the mcp_use library with MCPClient
to connect any LLM to MCP tools through a unified interface.

Special thanks to https://github.com/microsoft/playwright-mcp for the server.
"""

import asyncio
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from mcp_use import MCPAgent, MCPClient


async def main():
    """Run the example using a configuration file."""
    # Load environment variables
    load_dotenv()

    # Create MCPClient from config file
    client = MCPClient.from_config_file(os.path.join(os.path.dirname(__file__), "browser_mcp.json"))
    # Create LLM
    # llm = ChatOpenAI(model="gpt-4o")
    # llm = init_chat_model(model="llama-3.1-8b-instant", model_provider="groq")
    # llm = ChatAnthropic(model="claude-3-")
    llm = ChatGroq(model="qwen/qwen3.6-27b")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "find the best airbnb in Los Angeles with BROWSER USING GOOGLE SEARCH",
        max_steps=30,
    )
    print(f"\nResult: {result}")


if __name__ == "__main__":
    # Run the appropriate example
    asyncio.run(main())