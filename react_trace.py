"""Part B: print the agent's real ReAct trace for a multi-step canteen question."""
from agent import agent

QUESTION = ("Which is cheaper: samosa and tea with a 10% discount, "
            "or all five menu items with a 25% discount? By how much?")

print("QUESTION:", QUESTION, "\n")
print("--- the agent's actions and observations ---")
answer = agent(QUESTION, max_steps=12)
print("\nFINAL ANSWER:", answer)