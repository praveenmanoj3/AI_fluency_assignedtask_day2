"""A question none of the three systems was designed for."""
from workflow import workflow
from agent import agent

QUESTION = "I have Rs. 50. Which two items can I buy together within this budget?"

print("Q:", QUESTION)
print("\nWorkflow :", workflow(QUESTION))
print("\nAgent    :", agent(QUESTION))