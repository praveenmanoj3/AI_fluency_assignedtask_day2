"""Part C: the same reasoning questions asked WITHOUT and WITH Chain-of-Thought."""
from config import client, MODEL, banner

QUESTIONS = [
    # 1. Multi-step arithmetic
    "Three friends order food costing Rs. 45, Rs. 60 and Rs. 35. They get a 10% "
    "group discount on the total, split equally 3 ways. How much does each person pay?",
    # 2. Counting in two parts
    "A canteen counter can serve 4 students per minute in the morning rush and "
    "6 students per minute in the evening rush. How many students are served in "
    "a 10-minute morning rush and a 5-minute evening rush combined?",
    # 3. Ordering / logic
    "Meera's order costs more than Raj's. Raj's costs more than Sam's. Priya's "
    "costs less than Sam's. Who paid the most and who paid the least?",
]

DIRECT_PROMPT = "You are a helpful assistant. Give only the final answer. Do not explain."

COT_PROMPT = ("You are a helpful assistant. Solve the problem step by step. "
              "Number each step and show the calculation in that step. "
              "After the steps, write the last line exactly as: Final Answer: <answer>")

def ask(system_prompt, question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": system_prompt},
                  {"role": "user", "content": question}],
        temperature=0,
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    banner("CHAIN-OF-THOUGHT COMPARISON")
    for number, question in enumerate(QUESTIONS, start=1):
        print("=" * 72)
        print(f"QUESTION {number}: {question}\n")
        print("--- WITHOUT CoT ---")
        print(ask(DIRECT_PROMPT, question), "\n")
        print("--- WITH CoT ---")
        print(ask(COT_PROMPT, question), "\n")