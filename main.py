from fastmcp import FastMCP
import random
import json

mcp= FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: int, b:int)-> int:

    """
    Add two numbers

    Args:
    a:first number
    b:second number

    returns :
         the sum of a and b
    """
    return a+b


@mcp.tool
def random_generate()-> int:
    """
    Generate a random number between 0 and 1000
    """
    return random.randint(0,1000)



if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
