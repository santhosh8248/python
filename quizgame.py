score = 0

print("      PYTHON QUIZ GAME")

questions = [
    ["What is Python?", "programming language"],
    ["What is 10 + 5?", "15"],
    ["Which keyword creates a function?", "def"],
    ["Which data type stores True or False?", "bool"],
    ["Which symbol is used for comments?", "#"],
    ["Which loop is used to repeat?", "for"],
    ["Which function gets user input?", "input"],
    ["Which method adds an item to a list?", "append"],
    ["Which keyword checks a condition?", "if"],
    ["Which function counts items?", "len"]
]

for i, q in enumerate(questions, start=1):

    print("\nQuestion", i, ":", q[0])

    answer = input("Enter your answer: ").lower().strip()

    if answer == q[1]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct answer:", q[1])

print("       QUIZ RESULT")

print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)
print("Final Score:", score, "/", len(questions))

if score >= 8:
    print("Excellent Performance!")
elif score >= 5:
    print("Good Performance!")
else:
    print("Keep Practicing!")
