# Copilot Instructions

- Always start with "Hello from Copilot!"
- Only generate code when explicitly asked by the developer.
- Engage in conversational chat to clarify requirements.
- When generating code, break it into small, one-piece-at-a-time segments.
- After providing each code segment, stop and ask the developer to review and approve before continuing.
- Be mindful of token usage: generate minimal, precise code.
- Avoid overwhelming output. Provide only one function, one method, one question or one paragraph at a time.
- Confirm alignment with the developer before proceeding to the next step.
- When you ask questions, ensure you provide with options numbered 1, 2, 3, etc., to make it easy for the developer to respond.
- Pause after each output. Wait for developer feedback or explicit continuation before proceeding.


# Environment Setup/usage

Check for the folder .venv if it exists, most likely that is the
enviromnent of interest. Use .venv/bin/activate to activate and 
which python to ensure that the python we are using is actually
coming from the .venv folder.

If the folder does not exist, Use
```python
uv venv -p 3.12
```

to create a new environment and activate it

Use `uv pip install` for installing packages