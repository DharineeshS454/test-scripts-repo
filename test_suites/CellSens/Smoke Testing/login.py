"""
Dummy demo script for the 'login' feature.
Simulates running whichever test cases were checked in the UI, with a
randomized pass/fail per case -- purely for demoing the Run flow end to
end. Replace with real automation (Selenium/Playwright/API calls) once
CellSens/Preciv are actually available to test against.

Contract with app.py:
- Reads the list of selected test case names from the SELECTED_TEST_CASES
  env var (JSON array of strings).
- Prints one line starting with "RESULT_JSON:" followed by a JSON object
  with per-case results, so the UI can show pass/fail per checkbox.
- Exits 0 if every selected case passed, 1 if any failed.
"""
import json
import os
import random
import sys
import time

raw = os.environ.get("SELECTED_TEST_CASES", "[]")
try:
    selected_cases = json.loads(raw)
except json.JSONDecodeError:
    selected_cases = []

if not selected_cases:
    print("No test cases were selected.")
    sys.exit(1)

results = []
all_passed = True

for case_name in selected_cases:
    time.sleep(0.3)  # simulate the case actually doing something
    passed = random.random() > 0.3  # ~70% pass rate, feels realistic
    status = "pass" if passed else "fail"
    detail = "Completed successfully." if passed else "Assertion failed: unexpected result."
    print(f"[{status.upper()}] {case_name} - {detail}")
    results.append({"name": case_name, "status": status, "detail": detail})
    if not passed:
        all_passed = False

print("RESULT_JSON:" + json.dumps({"case_results": results}))
sys.exit(0 if all_passed else 1)
