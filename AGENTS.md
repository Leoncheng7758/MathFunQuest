# Engineering rules

- This repository is a Python/Kivy prototype. Counting is implemented; math and shape screens are placeholders.
- Keep scores in memory and preserve the existing 3–8 object range and three distinct choices.
- Render the quantity before asking for an answer. Accept each correct answer once and cancel scheduled work when leaving a screen.
- Use real Kivy widgets for interaction regressions; patch scheduling only for deterministic timer assertions.
- Run `ruff check .`, `python -m compileall -q main.py test_main.py`, `python -m unittest discover -v`, and `pip-audit -r requirements.txt` before committing.
- On headless Linux use `xvfb-run -a` for widget tests. Set `KIVY_HOME` to a writable directory.
- Do not add analytics, accounts, advertising, networking, or product features without an explicit requirement.
- Keep mobile packaging, touch testing, CJK font support, and accessibility limitations visible. Do not claim learning effectiveness.
- Use improvement branches and pull requests; never push to or merge into the default branch directly.
