# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 5
- Student name: Lee Hui Zhen
- Matric no: A24CS0259
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 14 November 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 14 November 2026, 8:30 AM
- Tool: Google (2026). Gemini. Retrieved 14 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "In sequence_utils.py, why do we call is_valid_dna inside gc_content and reverse_complement instead of checking the characters again?"
- Output: Explained that reusing is_valid_dna keeps the validation rule in one place, so empty strings and ambiguous N bases are handled consistently without duplicating code.
- Verified by: Checked Lab 5 Task T1 hint and tested gc_content("") and gc_content("ATGCN") to confirm both raise ValueError.
- My change: Called if not is_valid_dna(sequence): raise ValueError(...) at the start of both gc_content and reverse_complement.
- Used in: src/sequence_utils.py (gc_content, reverse_complement)

## Entry 2

- Date: 14 November 2026, 8:45 AM
- Tool: Google (2026). Gemini. Retrieved 14 November 2026 from https://gemini.google.com
- Purpose: debug
- Prompt: "When I run pytest on normalize.py, proportions gives NameError: name 'total' is not defined"
- Output: Pointed out that total was checked in `if total == 0:` before calculating `total = sum(counts)`, and also reminded to verify the file is spelled `normalize.py` with a z.
- Verified by: Added `total = sum(counts)` in proportions and ran `python -m pytest` to confirm visible tests pass.
- My change: Defined `total = sum(counts)` before the zero-total check in `src/normalize.py`.
- Used in: src/normalize.py (proportions)

## Entry 3

- Date: 14 November 2026, 9:00 AM
- Tool: Google (2026). Gemini. Retrieved 14 November 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: "How do I prove in pytest that proportions does not change the original input list?"
- Output: Suggested saving the input in a variable like `raw = [50, 30, 20]`, calling `result = proportions(raw)`, and asserting both `raw == [50, 30, 20]` and `result is not raw`.
- Verified by: Ran `python -m pytest` on `tests/test_lab05_own.py` and verified all assertions passed.
- My change: Wrote `test_proportions_input_unchanged_and_zero_total` checking both list equality and object identity.
- Used in: tests/test_lab05_own.py

## Entry 4

- Date: 14 November 2026, 9:15 AM
- Tool: Google (2026). Gemini. Retrieved 14 November 2026 from https://gemini.google.com
- Purpose: tests-plan
- Prompt: "What edge cases are not covered in test_visible.py that I should add into tests/test_lab05_own.py?"
- Output: Recommended testing zero and empty totals in proportions/cpm, explicit and negative library_size in cpm, allow_n=True vs False in is_valid_dna, and empty or oversized motifs in find_motif.
- Verified by: Cross-checked against Lab 5 Tasks T1 to T5 and rubric criteria R1 to R8.
- My change: Added four unit test functions covering both `normalize` and `sequence_utils` in `tests/test_lab05_own.py` and verified with `ruff check src tests`.
- Used in: tests/test_lab05_own.py