# CLAUDE.md — War-Criminals-Regardless

This file documents the repository structure, development conventions, and AI assistant guidelines for the War-Criminals-Regardless project.

## Project Overview

War-Criminals-Regardless is a planned pentesting/security toolkit designed for authorized security assessments and real-world situational use. The README describes it as a general-purpose utility for people navigating difficult or dangerous environments, including a security testing component.

**Current state**: Early-stage repository — only a README.md exists. No code has been written yet.

## Repository Structure

```
War-Criminals-Regardless-/
├── README.md       # Project description
└── CLAUDE.md       # This file
```

As the project grows, the expected layout is:

```
War-Criminals-Regardless-/
├── README.md
├── CLAUDE.md
├── src/            # Source code modules
├── tests/          # Test suite
├── docs/           # Extended documentation
└── requirements.txt / pyproject.toml / package.json (depending on language chosen)
```

## Git Workflow

- **Main branch**: `main` — stable, production-ready code only
- **Feature branches**: `<author>/<short-description>` (e.g., `claude/add-claude-documentation-oOLSB`)
- Always develop on a feature branch and open a PR into `main`
- Commit messages should be clear and imperative: `Add port scanner module`, `Fix timeout handling in SSH probe`
- Never force-push to `main`

## Development Conventions

### Language / Stack

The language and stack have not been decided yet. When the first code is added:
- Document the chosen language and runtime version here
- Add a dependency manifest (e.g., `requirements.txt`, `package.json`, `go.mod`)
- Add a `Makefile` or equivalent with standard targets: `build`, `test`, `lint`, `clean`

### Code Style

- Follow the style guide of whichever language is chosen (PEP 8 for Python, `gofmt` for Go, `eslint` for JS/TS)
- Keep functions small and focused — one clear responsibility per function
- Prefer explicit error handling over silent failures, especially for network operations and system calls
- No commented-out dead code; remove it entirely

### Testing

- All new modules must have accompanying tests
- Tests live in `tests/` and mirror the `src/` directory structure
- Run the full test suite before opening a PR

### Security and Ethics

This project is explicitly a security/pentesting toolkit. All contributors and AI assistants must follow these rules:

1. **Authorized use only** — every feature must be designed for use against systems the operator owns or has explicit written permission to test.
2. **No malware, ransomware, or destructive payloads** — tools that cause irreversible damage to third-party systems are out of scope.
3. **No mass-targeting capabilities** — features that automate attacks against arbitrary internet hosts are not acceptable.
4. **No detection evasion for malicious purposes** — stealth features are acceptable for authorized red-team engagements; building evasion purely to help bad actors is not.
5. **Document scope clearly** — every module's docstring or header comment must state what it does and under what authorization context it should be used.

When asked to implement a feature, AI assistants must refuse or flag anything that violates the above principles, even if framed as legitimate security research.

## Working with AI Assistants (Claude)

- This repo is developed with Claude Code assistance
- AI assistants should ask clarifying questions before writing any security-sensitive module to confirm the intended use case and authorization context
- Prefer small, reviewable commits over large monolithic changes
- When adding a new tool or module, also add its usage example to `README.md` or `docs/`
- Do not invent or guess URLs, IP addresses, or real target identifiers in example code — use placeholder values like `192.0.2.1` (RFC 5737 documentation range) or `target.example.com`

## Commands (to be updated as the project matures)

| Command | Purpose |
|---------|---------|
| _(TBD)_ | Run tests |
| _(TBD)_ | Lint / format code |
| _(TBD)_ | Build / package |

Update this table when the first real code and tooling are added.

## Contact

- Author: Damon (damondelatorres99@gmail.com)
- Repository: westsidemother12/war-criminals-regardless-
