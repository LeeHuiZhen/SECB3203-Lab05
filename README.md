# SECB3203 Lab 5 - Functions and modules: sequence_utils.py and normalize.py

Student: Lee Hui Zhen, A24CS0259

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/sequence_utils.py` : clean_sequence, is_valid_dna, gc_content, reverse_complement, find_motif
- `src/normalize.py` : proportions, cpm (never change the caller's data)
- `tests/` : visible tests and my own tests (test_lab05_own.py)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Design decisions
`proportions()` raises a `ValueError` when the total is zero because returning a list of zeros would look like valid biological data (no expression) instead of flagging an empty or failed sample. In `src/normalize.py`, the list comprehension `return [value / total for value in counts]` builds and returns a brand-new list rather than modifying `counts` in place, ensuring the caller's original list stays unchanged.