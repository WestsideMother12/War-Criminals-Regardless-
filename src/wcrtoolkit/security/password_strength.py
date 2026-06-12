"""Password strength evaluation utilities."""

from __future__ import annotations

import re
from dataclasses import dataclass, field

_COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "letmein", "monkey", "111111", "admin", "welcome",
}

_LABELS = ["very weak", "weak", "fair", "strong", "very strong"]


@dataclass
class PasswordStrengthResult:
    score: int
    label: str
    issues: list[str] = field(default_factory=list)


def evaluate_password(password: str) -> PasswordStrengthResult:
    """Score a password from 0 (very weak) to 4 (very strong)."""
    if not password:
        return PasswordStrengthResult(score=0, label=_LABELS[0], issues=["Password is empty."])

    issues: list[str] = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        issues.append("Password should be at least 8 characters long.")

    if len(password) >= 12:
        score += 1

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        issues.append("Use a mix of uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        issues.append("Include at least one digit.")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        issues.append("Include at least one symbol.")

    if password.lower() in _COMMON_PASSWORDS:
        score = 0
        issues.insert(0, "Password is a commonly used password.")

    score = max(0, min(score, 4))
    return PasswordStrengthResult(score=score, label=_LABELS[score], issues=issues)
