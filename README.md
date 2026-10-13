# Browser Agent Demo

A small app where you type a task in plain English and an AI agent
completes it in a real web browser. Every task and result is saved to results.txt.

## Built with
- [Browser Use](https://github.com/browser-use/browser-use), an open-source library
  for AI browser control (not written by me)
- Google Gemini as the AI model
- Python 3.11+

## What I built
- A command-line app that accepts any task from the user
- Result printing and timestamped logging to a file
- Setup and debugging: model errors, API quotas, bot blocking

## Run it
1. Install uv and Python 3.11+
2. uv venv --python 3.12
3. uv pip install -r requirements.txt
4. uvx playwright install chromium
5. Create a .env file containing GEMINI_API_KEY=your_key
6. uv run python my_agent.py

## Example tasks
- Open https://wttr.in/Delhi and tell me the current temperature
- Go to https://news.ycombinator.com and list the top 5 headlines

Author: Shruti Singh