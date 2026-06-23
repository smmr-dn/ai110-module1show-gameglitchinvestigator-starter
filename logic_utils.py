def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""

    # FIX: Corrected the ranges for each difficulty level to ensure they match the intended game design.
    
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100

def parse_guess(raw: str, low: int, high: int):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """

    #FIX: Added checks for decimal numbers and out-of-range values to ensure only valid whole number guesses are accepted.

    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            return False, None, "That is not a whole number."
        
        value = int(raw)
        if value < low or value > high:
            return False, None, f"Enter a number between {low} and {high}."
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """

    # FIX:
    # - Fixed inverted logic for "Too High" and "Too Low" outcomes.
    # - Removed dead-code for TypeError since guess is already converted to int

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go Lower!"
    else:
        return "Too Low", "📈 Go Higher!"



def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    
    # FIX: Updated scoring logic to ensure points are awarded correctly based on the attempt number and outcome.

    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High" or outcome == "Too Low":
        return current_score - 5

    return current_score
