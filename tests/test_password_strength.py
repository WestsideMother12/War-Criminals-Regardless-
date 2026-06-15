import pytest

from wcrtoolkit.security.password_strength import evaluate_password


def test_empty_password_is_very_weak():
    result = evaluate_password("")
    assert result.score == 0
    assert result.label == "very weak"
    assert result.issues == ["Password is empty."]


def test_common_password_scores_zero():
    result = evaluate_password("Password")
    assert result.score == 0
    assert "commonly used" in result.issues[0]


def test_short_password_flags_length_issue():
    result = evaluate_password("abc123")
    assert any("8 characters" in issue for issue in result.issues)


def test_missing_uppercase_flags_case_issue():
    result = evaluate_password("alllowercase1!")
    assert any("uppercase and lowercase" in issue for issue in result.issues)


def test_missing_digit_flags_digit_issue():
    result = evaluate_password("NoDigitsHere!")
    assert any("digit" in issue for issue in result.issues)


def test_missing_symbol_flags_symbol_issue():
    result = evaluate_password("NoSymbolsHere1")
    assert any("symbol" in issue for issue in result.issues)


def test_strong_password_has_no_issues():
    result = evaluate_password("Tr0ub4dor&3xyz")
    assert result.score == 4
    assert result.label == "very strong"
    assert result.issues == []


@pytest.mark.parametrize(
    "password, expected_score",
    [
        ("", 0),
        ("abc", 0),
        ("abcdefgh", 1),
        ("abcdefghijkl", 2),
        ("Abcdefgh1", 3),
        ("Abcdefg1!", 4),
    ],
)
def test_score_progression(password, expected_score):
    assert evaluate_password(password).score == expected_score
