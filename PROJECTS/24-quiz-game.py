# Python quiz game

questions = ("What is Batman's secret identity?",
             "What is the name of Superman's home planet?",
             "Who is Batman's loyal butler and closest confidant?",
             "What is Superman's primary weakness?",
             "Which city does Superman primarily protect?")

options = (("A. Clark Kent", "B. Bruce Wayne", "C. Peter Parker", "D. Tony Stark"),
           ("A. Krypton", "B. Mars", "C. Gotham", "D. Asgard"),
           ("A. Jarvis", "B. Alfred Pennyworth", "C. Happy Hogan", "D. Sebastian"),
           ("A. Magic", "B. Kryptonite", "C. Lead", "D. Red Sun Radiation"),
           ("A. Gotham City", "B. Central City", "C. Metropolis", "D. Star City"))

answers = ("B", "A", "B", "B", "C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guesses[question_num] == answers[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer!")


    question_num += 1

print("-------------------------------")
print("            RESULT             ")
print("-------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")