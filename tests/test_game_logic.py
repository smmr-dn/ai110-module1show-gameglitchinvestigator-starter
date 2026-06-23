from logic_utils import check_guess, parse_guess, update_score


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- parse_guess ---

def test_parse_guess_valid_integer():
    ok, value, _ = parse_guess("42", 1, 100)
    assert ok is True
    assert value == 42

def test_parse_guess_empty_string():
    ok, _, _ = parse_guess("", 1, 100)
    assert ok is False

def test_parse_guess_none():
    ok, _, _ = parse_guess(None, 1, 100)
    assert ok is False

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert err == "That is not a number."

def test_parse_guess_decimal_rejected():
    ok, _, err = parse_guess("7.9", 1, 100)
    assert ok is False
    assert err == "That is not a whole number."

def test_parse_guess_decimal_whole_number_rejected():
    ok, _, err = parse_guess("3.0", 1, 100)
    assert ok is False
    assert err == "That is not a whole number."

def test_parse_guess_above_range_rejected():
    ok, _, err = parse_guess("150", 1, 100)
    assert ok is False
    assert err == "Enter a number between 1 and 100."

def test_parse_guess_below_range_rejected():
    ok, _, err = parse_guess("0", 1, 100)
    assert ok is False
    assert err == "Enter a number between 1 and 100."

def test_parse_guess_at_range_boundary_low():
    ok, value, _ = parse_guess("1", 1, 100)
    assert ok is True
    assert value == 1

def test_parse_guess_at_range_boundary_high():
    ok, value, _ = parse_guess("100", 1, 100)
    assert ok is True
    assert value == 100


# --- update_score ---

def test_update_score_win_early():
    result = update_score(0, "Win", 0)
    assert result == 100

def test_update_score_win_minimum_points():
    # attempt 9 → 100 - 10*9 = 10, clamped to 10
    result = update_score(0, "Win", 9)
    assert result == 10

def test_update_score_too_low_penalizes():
    result = update_score(50, "Too Low", 0)
    assert result == 45

def test_update_score_too_high_odd_penalizes():
    result = update_score(50, "Too High", 1)
    assert result == 45

def test_update_score_too_high_even_bug():
    result = update_score(50, "Too High", 0)
    assert result == 45 
