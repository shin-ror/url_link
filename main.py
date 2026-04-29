from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo 🚀",port=9000)

@mcp.tool()
def add(a, b):
    """
    加法測試
    """
    return a + b

if __name__ == "__main__":
    mcp.run(transport="sse")