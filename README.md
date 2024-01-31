# DevDocGenie
---
![DocDevGenie](https://repository-images.githubusercontent.com/721810725/52be4ec9-0672-415e-b2e9-74e569843e0e)

---
**DocDevGenie**: Always-Updated API Assistance for Developers

DocDevGenie revolutionizes API documentation access for developers by addressing a critical gap in existing LLM-based AI tools.

Traditional tools often rely on outdated versions of API documentation, which can be problematic given the rapid evolution of popular libraries and frameworks.

**DocDevGenie** stands out by intelligently detecting project dependencies, ensuring that developers receive the most current and relevant documentation assistance.

This dynamic approach guarantees up-to-date support, streamlining the development process and enhancing productivity.

---

## How it works


## How to run the MVP

1. Run Ollama locally.
2. Run mistral when running for the first time.
3. To run mistral execute `ollama run mistral`.
4. Get inside the mvp folder.
5. Run `python3 -m venv env` to create a virtual environment.
6. Run `source env/bin/activate` for MAC users to activate the virtual environment.
7. Run `pip install llama-index qdrant_client torch transformers` to install the dependencies.
8. Run `python index.py` to execute the code.
