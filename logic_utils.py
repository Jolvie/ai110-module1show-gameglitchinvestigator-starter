def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    Includes a progression where harder difficulties have wider ranges.

    #FIX: Refactored range logic into logic_utils.py as part of AI collaboration (Copilot suggested separation for testability).
    """

    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 500

    return 1, 100


def parse_guess(raw: str):
    """Parse user input into an int guess.

    Returns:
        (ok: bool, guess_int: int | None, error_message: str | None)
    """

    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare guess to secret and return (outcome, message)."""

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    Scoring rules:
      - Win: base 100 points, minus 10 for each extra attempt (minimum 10).
      - Incorrect guess: -5 points.

    #FIX: Simplified scoring logic based on discussion with AI; removed inconsistent parity-based penalties.
    """

    if outcome == "Win":
        points = max(10, 100 - (attempt_number - 1) * 10)
        return current_score + points

    return current_score - 5
