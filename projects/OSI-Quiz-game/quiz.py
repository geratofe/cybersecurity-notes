#!/usr/bin/env python3
# ============================================================
#   OSI MODEL QUIZ GAME
#   - 50 random questions per game
#   - 2 points per correct answer = 100 points max
#   - Questions are shuffled so you never repeat the same set
# ============================================================

import json    # lets us read the questions.json file
import random  # lets us shuffle and pick random questions


# ── STEP 1: LOAD QUESTIONS FROM FILE ─────────────────────────
# open() opens the file, json.load() reads it into a Python list
with open("questions.json") as file:
    all_questions = json.load(file)


# ── STEP 2: WELCOME SCREEN ───────────────────────────────────
print("=" * 50)
print("       WELCOME TO THE OSI MODEL QUIZ!")
print("=" * 50)
print("  50 questions  |  2 points each  |  100 points max")
print("=" * 50)
input("\nPress ENTER to start the quiz...")  # waits for the player to press Enter


# ── STEP 3: PICK 50 RANDOM QUESTIONS ─────────────────────────
# random.sample() picks 50 unique questions from the full list
# this means you won't see the same question twice in one game
selected_questions = random.sample(all_questions, 50)


# ── STEP 4: SET UP SCORE COUNTER ─────────────────────────────
score = 0  # starts at 0, goes up by 2 for every correct answer


# ── STEP 5: LOOP THROUGH ALL 50 QUESTIONS ────────────────────
# enumerate() gives us a counter (i) starting at 1
for i, question in enumerate(selected_questions, start=1):

    print("\n" + "-" * 50)
    # show question number and the question text
    print(f"Question {i} of 50: {question['question']}")
    print()

    # show the 4 answer options (A, B, C, D)
    for option in question["options"]:
        print(f"  {option}")

    print()

    # ── STEP 6: GET PLAYER'S ANSWER ──────────────────────────
    # keep asking until the player types A, B, C, or D
    while True:
        answer = input("Your answer (A / B / C / D): ").strip().upper()
        # .strip() removes accidental spaces, .upper() makes it capital

        if answer in ["A", "B", "C", "D"]:
            break  # valid answer, exit the while loop
        else:
            print("  ⚠  Please type A, B, C, or D only.")

    # ── STEP 7: CHECK IF ANSWER IS CORRECT ───────────────────
    if answer == question["answer"]:
        print("  ✅  Correct! +2 points")
        score += 2  # add 2 points to the score
    else:
        # show the correct answer so the player can learn
        print(f"  ❌  Wrong! The correct answer was: {question['answer']}")


# ── STEP 8: SHOW FINAL SCORE ──────────────────────────────────
print("\n" + "=" * 50)
print("           QUIZ COMPLETE!")
print("=" * 50)
print(f"  Your final score: {score} / 100")
print()

# give a message based on how well the player did
if score == 100:
    print("  🏆  Perfect score! You're an OSI master!")
elif score >= 80:
    print("  🌟  Great job! You really know your layers!")
elif score >= 60:
    print("  👍  Good effort! Keep studying and you'll ace it!")
elif score >= 40:
    print("  📖  Not bad! Review the OSI layers and try again.")
else:
    print("  💪  Keep practicing! You'll get there!")

print("=" * 50)
input("\nPress ENTER to exit.")  # keeps the window open until you press Enter
