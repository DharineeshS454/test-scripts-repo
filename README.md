# Test Suites Repository — Structure Guide

This repo is pulled by the Test Runner app. Folder layout is important —
the app reads it directly to build the UI.

## Folder convention

```
test_suites/
  <Application>/
    <Test Type>/
      <feature>.py                 # the script that gets executed
      <feature>_test_cases.xlsx    # test cases shown as checkboxes in the UI
```

Scripts and their workbook sit **directly** inside the Test Type folder,
paired by matching base name — no extra subfolder per feature.

- **`<Application>`** — e.g. `CellSens`, `Preciv`. Must exactly match the
  application name configured in the app's "Application" dropdown.
- **`<Test Type>`** — must be exactly one of: `Regression Testing`,
  `Smoke Testing`, `Sanity Testing`, `Integration Testing`.
- **`<Feature>`** — a subfolder per feature/screen being tested (e.g. `login`,
  `dashboard`, `reports`). This is the folder name shown when a user expands
  a Test Type.
- **`<feature>_test_cases.xlsx`** — one row per test case. Columns:
  - `Test Case Name` — shown as the checkbox label in the UI
  - `Description` — what the test does (optional, for reference)
  - `Expected Result` — what a pass looks like (optional, for reference)
- **`<feature>.py`** — the actual script. Must exit with code `0` for pass,
  non-zero for fail. Runs via `python <file>.py`.

## Adding a new feature

1. Copy `login.py` and `login_test_cases.xlsx` into the right
   `<Application>/<Test Type>/` folder.
2. Rename both to your feature, keeping the same base name — e.g.
   `dashboard.py` and `dashboard_test_cases.xlsx`.
3. Edit the Excel rows to your real test cases (the `Test Case Name` column
   drives the checkboxes shown in the UI).
4. Edit the `.py` script to actually perform the test. It receives the
   checked test case names via the `SELECTED_TEST_CASES` env var (a JSON
   array of strings) and should print a line like:
   `RESULT_JSON:{"case_results": [{"name": "...", "status": "pass", "detail": "..."}]}`
   so the UI can show a pass/fail per test case, not just per script.

## Adding a new application

Duplicate the whole `CellSens/` folder, rename it, and make sure the name
matches exactly what's added via "+ Add application" in the app UI.
