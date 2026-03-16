# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - Give you the wrong hint
  - New game does not wipe the history and does not really restart the game
  - The level bounds are not actually working, they give random number between 0 and 100 despite the difficulty

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  -I used Copilot as my primary AI tool for this project. I leveraged it to understand the existing code, identify potential bugs, and get suggestions for fixes. Additionally, I used it to help me design tests and understand Streamlit's session state to address the issue of the secret number changing.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - One example of a correct AI suggestion was when I asked Copilot about how to maintain state in Streamlit. It suggested using Streamlit's session state to store the secret number, which would prevent it from changing every time the app reruns. I implemented this suggestion by assigning the secret number to a session state variable, and after testing the game, I found that the secret number remained stable across interactions, confirming that the AI's suggestion was effective in fixing that particular bug.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - One example of an incorrect AI suggestion was when I asked Copilot to help me with the newGame logic. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
When I could test it manually by playing the game and seeing that the bug was no longer present, I considered it fixed. For example, after fixing the hint logic, I would make a guess and check if the hint provided was correct (i.e., if my guess was too high, the hint should say "Lower", and if it was too low, it should say "Higher"). If the hints were accurate based on my guesses, I would conclude that the bug was fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
After refactoring the logic into `logic_utils.py`, I ran `pytest` to ensure that all the tests were passing. For instance, I had a test that checked if the scoring logic was correct based on the number of attempts. When I ran this test, it failed initially, indicating that there was still an issue with the scoring logic. After reviewing the code and making necessary adjustments, I ran the test again, and it passed successfully, confirming that the scoring logic was now working as intended.
- Did AI help you design or understand any tests? How?
Yes, AI helped me design tests by suggesting specific scenarios to test for, such as edge cases where the player's guess is exactly the secret number or when the guess is just one number away from the secret number. The AI also provided insights into how to structure the tests effectively, ensuring that they covered a range of inputs and conditions. This guidance was instrumental in helping me create comprehensive tests that thoroughly evaluated the functionality of the game logic.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing in the original app because Streamlit reruns the entire script from top to bottom every time a user interacts with the app, such as clicking a button. This means that any variables defined in the script will be reset to their initial values on each interaction, which is why the secret number was not stable and kept changing every time the user clicked "Submit".
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the entire script from top to bottom every time a user interacts with the app, such as clicking a button or changing a selection. This means that any variables defined in the script will be reset to their initial values on each interaction, which is why the secret number kept changing in the original app. To maintain state across these reruns, Streamlit provides a feature called session state, which allows you to store and persist data (like the secret number) across interactions, ensuring that it doesn't reset every time the app reruns.
- What change did you make that finally gave the game a stable secret number?
I implemented Streamlit's session state to store the secret number. By assigning the secret number to a session state variable, it persists across reruns of the app, ensuring that the secret number remains stable and does not change every time the user interacts with the app. This way, players can have a consistent experience while trying to guess the number without it resetting unexpectedly.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - For example: "I want to remember to write tests for my code before I start writing the code itself" or "I want to remember to ask the AI to explain its reasoning when it gives me a suggestion, so I can learn from it."
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would try to the problem myself first before asking the AI for help. This way, I can better understand the issue and have a clearer idea of what I need assistance with when I do ask the AI. It would also allow me to learn more from the process of debugging and problem-solving on my own before leveraging AI as a tool to enhance my understanding and find solutions.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - I used to think that AI-generated code was bad and should never be used by developers, but now I see that it can be a helpful tool when used correctly. It can provide useful suggestions and help me understand concepts better, but it's important to verify the AI's suggestions and not rely on it blindly, as it can also produce incorrect or misleading code.




## Bugs:

- Give you the wrong hint
- New game does not wipe the history and does not really restart the game
- The level bounds are not actually working, they give random number between 0 and 100 despite the difficulty

