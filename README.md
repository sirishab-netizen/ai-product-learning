Project: AI product learning

Run instructions for the `learning` examples:

- From the workspace root, run the `main` module as a package (recommended):

```powershell
C:/Users/siris/AppData/Local/Python/pythoncore-3.14-64/python.exe -m learning.week1.day2.main
```

- Or set `PYTHONPATH` to the workspace root and run the script directly:

```powershell
$env:PYTHONPATH = "C:\\Users\\siris\\Documents\\ai-product-learning"
C:/Users/siris/AppData/Local/Python/pythoncore-3.14-64/python.exe learning/week1/day2/main.py
```

Notes:
- Using `python -m` ensures package imports (absolute or relative) work consistently.
- The repository now contains `__init__.py` files under `learning/`, `learning/week1/`, and `learning/week1/day2/`.

Direct script support:

- `main.py` now supports being run directly as a script without setting `PYTHONPATH` by falling back to adding the workspace root to `sys.path` when necessary. From the workspace root you can run:

```powershell
C:/Users/siris/AppData/Local/Python/pythoncore-3.14-64/python.exe learning/week1/day2/main.py
```
# AI Product Learning

This repository documents my 90-day journey to become an AI Product Leader.

## Goals

- Learn Python
- Build AI products
- Master LLMs
- Build production-grade AI applications
- Showcase projects for AI Product Management roles

## Roadmap

- Week 1: Python & APIs
- Week 2: FastAPI & OpenAI
- Week 3–5: AI Travel Copilot
- Week 6–8: AI Fraud Investigation Agent
- Week 9–10: Payment Rules AI Builder
- Week 11–12: Portfolio & Deployment
