"""Tools the agent is allowed to use, plus their JSON Schema descriptions."""
import ast
import operator
from config import MENU_PRICES

def get_item_price(item_name: str) -> str:
    """Look up the price for one menu item."""
    price = MENU_PRICES.get(item_name.strip().upper())
    return str(price) if price is not None else f"Unknown item: {item_name}"

# A safe calculator: only numbers and + - * / ( ) are allowed. Never use eval().
_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.USub: operator.neg}

def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.left), _evaluate(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.operand))
    raise ValueError("Unsupported expression")

def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression such as (60 + 20) * 0.8."""
    try:
        return str(_evaluate(ast.parse(expression, mode="eval").body))
    except Exception as error:
        return f"Calculator error: {error}"

TOOL_FUNCTIONS = {"get_item_price": get_item_price, "calculator": calculator}

TOOLS = [
    {"type": "function", "function": {
        "name": "get_item_price",
        "description": "Get the price in rupees for a single canteen item, for example SANDWICH.",
        "parameters": {"type": "object",
                        "properties": {"item_name": {"type": "string"}},
                        "required": ["item_name"]}}},
    {"type": "function", "function": {
        "name": "calculator",
        "description": "Evaluate an arithmetic expression using + - * / and brackets.",
        "parameters": {"type": "object",
                        "properties": {"expression": {"type": "string"}},
                        "required": ["expression"]}}},
]

if __name__ == "__main__":
    print("get_item_price('sandwich') ->", get_item_price("sandwich"))
    print("calculator('(60 + 20) * 0.8') ->", calculator("(60 + 20) * 0.8"))
    print("calculator('60 - 40') ->", calculator("60 - 40"))