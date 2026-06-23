# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.

  **Game Glitch Investigator** is a number-guessing game built with Streamlit. The player picks a difficulty (Easy: 1–20, Normal: 1–50, Hard: 1–100), then guesses the secret number within a limited number of attempts. After each guess the game returns a "Too High" or "Too Low" hint. The player wins by guessing correctly before running out of attempts, and earns more points the fewer guesses they need.

- [x] Detail which bugs you found.

  | # | Bug | Symptom |
  |---|-----|---------|
  | 1 | Secret number re-rolled on every rerun | Secret changed each time the Submit button was clicked, making it impossible to win |
  | 2 | Inverted hints | Guessing too high showed "Go Higher"; guessing too low showed "Go Lower" |
  | 3 | Attempt counter off by one | First guess still showed full attempt count; counter only updated on the next submit |
  | 4 | New Game didn't reset score, status, or history | Score and game-over state carried over from the previous game |
  | 5 | Enter key didn't submit the form | Players had to click "Submit Guess" with the mouse; pressing Enter did nothing |
  | 6 | No range validation | Out-of-range numbers (e.g. 0 or 999) were silently accepted |
  | 7 | Decimals silently truncated | Entering "7.9" was accepted as 7 with no warning |
  | 8 | Difficulty ranges incorrect | Range boundaries didn't match the intended Easy / Normal / Hard design |
  | 9 | Scoring formula wrong | Points calculation used `attempt_number + 1` instead of `attempt_number - 1`, under-rewarding early wins |

- [x] Explain what fixes you applied.

  - **Session state for secret** — wrapped `st.session_state.secret` in an `if "secret" not in st.session_state` guard so it is only generated once per game.
  - **Corrected hint logic** — fixed the comparison in `check_guess`: `guess > secret` now returns "Too High" and `guess < secret` returns "Too Low".
  - **Attempt counter** — moved the `attempts += 1` increment to happen before the display check so the count is accurate immediately.
  - **Full state reset on New Game** — added `score`, `status`, and `history` to the reset block alongside `attempts` and `secret`.
  - **Form + Enter key** — wrapped the input and button in `st.form` so pressing Enter submits the guess.
  - **Range & decimal validation** — updated `parse_guess(raw, low, high)` to reject decimals ("That is not a whole number.") and out-of-range values ("Enter a number between {low} and {high}.").
  - **Difficulty ranges** — corrected `get_range_for_difficulty` so Easy = 1–20, Normal = 1–50, Hard = 1–100.
  - **Scoring formula** — changed `100 - 10 * (attempt_number + 1)` to `100 - 10 * (attempt_number - 1)` so a first-attempt win awards the full 100 points.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Choose a game difficulty level.
2. User enters a number, e.g. 40 for "Normal"
3. Game returns "Too High".
4. User enters 35.
5. Game returns "Too High".
6. User guesses until the game returns "Correct!".

## 🧪 Test Results

![alt text](<test_results.png>)

## 🚀 Stretch Features

- [x] Code fences/checks for decimal or out-of-range numbers/guesses. Tests were also added.
