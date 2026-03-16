from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 500)


def test_parse_guess_valid_and_invalid():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

    ok, value, err = parse_guess("not a number")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_update_score_win_and_losses():
    # Winning on first attempt gives full 100
    assert update_score(0, "Win", 1) == 100
    # Winning on second attempt gives 90
    assert update_score(0, "Win", 2) == 90
    # Winning late still gives minimum 10
    assert update_score(0, "Win", 20) == 10
    # Incorrect guess subtracts points
    assert update_score(100, "Too High", 1) == 95
    assert update_score(100, "Too Low", 1) == 95
