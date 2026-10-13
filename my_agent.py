from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

llm = ChatGoogle(model="gemini-3.8-flash")

while True:
    task = input("\nWhat should the agent do? (type 'exit' to quit) ")
    if task.strip().lower() == "exit":
        break
    agent = Agent(task=task, llm=llm)
    history = agent.run_sync()
    result = history.final_result()
    print("\nRESULT:", result)
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now():%Y-%m-%d %H:%M}] TASK: {task}\n{result}\n\n")