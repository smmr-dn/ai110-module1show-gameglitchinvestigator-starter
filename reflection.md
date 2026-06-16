# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The hints do not match the secret number. When the guesses go to the bounds (1 or 100), the hints still say "Go LOWER" or "Go HIGHER". Also, the guess attempts counter updates slower than it should be. For example, if I submit the first guess, the counter still says I have 7 attempts left. Not until do I submit the second guess, does the counter updates to 6.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess submitted | Attempt left to show 6 | Attempt left shows 7 | None |
| 78 (Secret number is 76) | Shows "Go LOWER" | Shows "Go HIGHER" | None |
| 71 (Secret number is 76) | Shows "Go HIGHER" | Shows "Go LOWER" | None |
| Reset the game | The score says "0" | The score says "-5" | None |

---

## 2. How did you use AI as a teammate?

I used Claude Code for this project. One example that the AI suggestion was correct was that the "New Game" handler at app.py and only "attempts" and "secret" were reset, but "score", "status", and "history" were never cleared. It said whatever score the player had at the end of the previous game carried over into the new one.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
