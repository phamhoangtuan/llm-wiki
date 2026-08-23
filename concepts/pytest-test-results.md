---
title: "pytest Test Results"
type: concept
tags: [python, testing, pytest, output]
created: 2026-05-23
updated: 2026-06-15
sources: [okken-python-testing-pytest]
---

## Summary

pytest provides a rich symbol system for understanding test suite status at a glance — beyond simple pass/fail.

## Result Symbols

| Symbol | Name | Meaning | When |
| --- | --- | --- | --- |
| `.` | PASSED | Test succeeded | Logic correct, assertion passes |
| `F` | FAILED | AssertionError | Logic wrong, data mismatch |
| `s` | SKIPPED | Intentionally skipped | `@pytest.mark.skip()` or `skipif` |
| `x` | XFAIL | Expected failure | `@pytest.mark.xfail()` for known issues |
| `X` | XPASS | Unexpected pass | Marked xfail but passed — review needed |
| `E` | ERROR | Exception outside test | Fixture/hook failure — infrastructure problem |
---
- Related to [[pytest-basics]] — understanding output is essential for reading test results
- Related to [[pytest-markers]] — skip and xfail are marker-driven results
- Related to [[pytest-assertions]] — assertion failures produce FAILED results with rich diffs
