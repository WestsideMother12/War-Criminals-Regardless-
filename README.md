# War-Criminals-Regardless-
This will be a pentesting program that will be able to do whatever you need for irl situations and should get you by in a pinch or maybe even get in to a warm building for the people in snowy areas but there is always badguys so to get this is to be vigilent and steer the bad guys away good luck and good hunting

## Project layout

- `src/wcrtoolkit/` - Python package
  - `security/password_strength.py` - password strength evaluation
  - `recon/port_scanner.py` - TCP connect-scan utilities (only use against systems you own or are authorized to test)
  - `cli.py` - command-line entry point (`wcrtoolkit`)
- `tests/` - pytest test suite

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Running tests

```bash
pytest --cov --cov-report=term-missing
```

CI runs the same test suite with coverage on every push and pull request (see `.github/workflows/ci.yml`).
