"""System 2: a rule-based workflow. Fixed if/else rules, no LLM at all."""
import re
from config import MENU_PRICES, QUESTIONS

def workflow(question):
    text = question.upper()
    items = [item for item in MENU_PRICES if item in text]
    fees = [MENU_PRICES[item] for item in items]

    if not fees:
        return "Sorry, I can only answer questions about menu prices."

    lower = question.lower()
    if "total" in lower:
        total = sum(fees)
        percent = re.search(r"(\d+)\s*%", lower)
        if "discount" in lower and percent:
            total = total * (1 - int(percent.group(1)) / 100)
        return f"Total cost: Rs. {total:,.0f}"

    if len(fees) == 1:
        return f"Price of {items[0].title()}: Rs. {fees[0]:,}"

    return "Sorry, I do not have a rule for this type of question."

if __name__ == "__main__":
    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW (no LLM) ===\n")
    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)