# Copilot instructions

## Project shape

This repository is a collection of standalone Python lesson scripts, not an installed package or application. Each file focuses on a topic—basic syntax, operators and conditionals, lists, tuples and sets, dictionaries and loops, or functions—and may combine commented teaching examples with a small active example. Read the relevant script and preserve that lesson-oriented structure when making changes; there is no shared application entry point or cross-file architecture.

Several scripts run interactively or print output as soon as they execute. Run the specific lesson script directly rather than importing it to explore its behavior. In particular, `list.py` has the same name as Python's standard-library `list` module, so avoid importing it as a module.

## Running and checking examples

Run a lesson from the repository root with:

```powershell
python Basic.py
```

Replace `Basic.py` with the script you want to explore. Scripts that prompt for input need corresponding input in the terminal.

There is no configured test suite, linter, or project dependency setup. To check one script for syntax errors without running its interactive examples:

```powershell
python -m py_compile Basic.py
```

## Conventions in the lessons

- Examples and explanations are kept close together in the topic script; many experiments are intentionally retained as commented-out code.
- The uncommented statements are the examples that run, so check which code is active before changing a script's behavior.
- Keep examples self-contained and use the standard library unless a lesson specifically calls for another dependency.
