def quiz():
    questions = {
        "Capital of India?": "delhi",
        "5 + 3 = ?": "8",
        "Python is a programming language? (yes/no)": "yes"
    }

    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ").lower().strip()

        if user_answer == answer:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer:", answer, "\n")

    print(f"Final Score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()
