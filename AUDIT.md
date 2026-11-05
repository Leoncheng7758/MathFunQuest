# Audit — 2026-11-05

Baseline: `7bc727a3a9421720b7874b6c62b33d33ce6093da` on `main`.

## Baseline evidence

- Two tracked files: README and `main.py`; no dependency manifest, tests, or Actions workflows.
- `python -m unittest discover -v`: 0 tests, exit 5 in this runner; no test coverage existed.
- `ruff check --select F .`: failed on an unused Image import.
- Constructing `MathFunQuestApp().build()` with real Kivy 2.3.1 succeeded.
- Six added counting regressions all errored on the unmodified source. Imported use of the correct-answer callback raised `NameError` for Clock; the displayed quantity and return button did not exist.

## Findings and changes

- P1: The quantity was randomly chosen but never rendered. Display that quantity as dots and restore the question on each round.
- P1: Repeated correct-answer callbacks could increment the score and schedule multiple rounds. Lock the round and disable choices after the first correct answer.
- P1: Clock was only imported in the script entry point. Import it at module scope so imported app instances work.
- P2: Counting had no return navigation and pending timers were not cancelled on leaving. Add a menu button and cancel pending work while preserving the accumulated score.
- P2: Missing dependency declaration and automated checks. Pin the tested Kivy version and add regression/quality CI with read-only permissions and pinned actions.

## Verification scope

Six real-widget regression tests cover imported use, displayed quantities 3–8, distinct choices, single scoring/timer, question reset, timer cancellation, and return navigation. Tests patch animation and scheduler calls for determinism; they do not replace Kivy widgets. Compilation and lint apply to the Python prototype. Record local and remote execution evidence in the PR.

Remaining: physical touch testing, font assets, responsive layouts, screen-reader behavior, mobile packaging, and implementation of the math/shape activities. No coverage percentage is claimed. No child-safety or learning-effectiveness certification is claimed. Advisory scans cover declared dependencies at scan time and do not prove absence of vulnerabilities.
