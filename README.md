# MathFunQuest
数学益智冒险 - 儿童计数加减形状学习游戏

## Current implementation

Python/Kivy prototype with a menu and a counting activity. Count the displayed dots and choose one of three numbers. Correct answers award one point and advance after 1.5 seconds. The math and shape screens remain placeholders.

`main.py` contains the screens, in-memory score, and application entry point. `test_main.py` exercises real widgets and the counting lifecycle. No storage, account, telemetry, or network API is implemented in this source.

## Development and running

Use Python 3.12 and a graphical desktop with OpenGL support:

```sh
python -m venv .venv
# Activate the environment using the command for your shell.
python -m pip install -r requirements-dev.txt
python main.py
```

The only application dependency is Kivy 2.3.1. It satisfies the existing Kivy 2.3.0 minimum. No credentials or environment configuration are required. Kivy writes framework settings and logs to its user directory; optionally set `KIVY_HOME` to another writable directory. Framework installation may use the network.

## Validation

```sh
ruff check .
python -m compileall -q main.py test_main.py
python -m unittest discover -v
pip-audit -r requirements.txt
```

On headless Linux, install Xvfb and run `xvfb-run -a python -m unittest discover -v`. CI runs lint, compilation, widget regressions, and a dependency advisory check. Compilation validates Python sources; no Android/iOS packaging configuration exists, and compilation is not a mobile build.

## Security and limitations

- No app-level personal data collection or persistence is present. This is a source observation, not certification of third-party framework behavior.
- Chinese text and emoji require suitable fonts; no CJK font is bundled. Dots avoid relying on emoji to convey the count.
- The existing 800×600 window and fixed font sizes need testing on real phones/tablets. Screen-reader support and touch accessibility have not been verified.
- Do not publish as a complete educational app: two activities are placeholders and no educational effectiveness has been measured.
- There is no release package, app-store configuration, or mobile build pipeline.

See [AUDIT.md](AUDIT.md) for the baseline, fixes, and remaining risks.
