import random
import streamlit as st

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
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
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    Scoring rules:
    - On a win, award points based on how quickly the player guessed.
      The earliest win gives 100 points, and each additional attempt reduces
      the win bonus by 10 points (minimum 10).
    - On any incorrect guess, subtract 5 points.

    This keeps scoring predictable and easy to explain.
    """

    if outcome == "Win":
        # attempt_number is 1-based (first guess is attempt 1)
        points = max(10, 100 - (attempt_number - 1) * 10)
        return current_score + points

    # Any wrong guess costs points
    return current_score - 5

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Everything that was off was fixed by Joel.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

low, high = get_range_for_difficulty(difficulty)

if "game_id" not in st.session_state:
    st.session_state.game_id = 0

if "current_difficulty" not in st.session_state:
    st.session_state.current_difficulty = difficulty

if st.session_state.current_difficulty != difficulty:
    # Difficulty changed, reset game.
    # FIX: Added difficulty-change reset logic based on AI and user feedback so the UI restarts cleanly.
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.current_difficulty = difficulty
    st.session_state.game_id += 1
    st.session_state.end_error = False
    st.success("Difficulty changed. New game started.")
    st.rerun()

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "end_message" in st.session_state:
    if st.session_state.get("end_balloons"):
        st.balloons()
    # FIX: Show end-game summary in one place, using markdown to prevent st.error being overwritten.
    if st.session_state.get("end_error"):
        st.markdown(
            f"<div style=\"background:#ff000038;border:1px solid #ff4d4d;padding:12px;border-radius:6px;\">\n"
            f"<strong>{st.session_state.end_message}</strong>\n"
            f"</div>",
            unsafe_allow_html=True,
        )
    else:
        st.success(st.session_state.end_message)

    for key in ["end_message", "end_balloons", "end_error"]:
        if key in st.session_state:
            del st.session_state[key]

st.subheader("Make a guess")

attempts_used = st.session_state.attempts

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}_{st.session_state.game_id}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀", disabled=st.session_state.status != "playing")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        attempts_used += 1
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.session_state.status = "won"
            st.session_state.end_message = (
                f"🎉 Correct!\n\n"
                f"You won! The secret was {st.session_state.secret}.\n"
                f"Final score: {st.session_state.score}.\n\n"
                f"Click \"New Game\" to play again."
            )
            st.session_state.end_balloons = True
            st.session_state.end_error = False
            st.rerun()
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.session_state.end_message = (
                    f"Game over.\n\n"
                    f"Out of attempts!\n"
                    f"The secret was {st.session_state.secret}.\n"
                    f"Score: {st.session_state.score}.\n\n"
                    f"Click \"New Game\" to play again."
                )
                st.session_state.end_error = True
                st.rerun()

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - attempts_used}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.game_id += 1
    st.success("New game started.")
    st.rerun()

st.divider()
st.caption("Built by an AI that claims this code is production-ready. But it wasn't until Joel fixed the glitches.")
