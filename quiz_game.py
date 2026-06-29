import time

def run_quiz():
    # 1. Interactive Age Checker
    print("====================================")
    print("      WELCOME TO THE TRIVIA GAME    ")
    print("====================================\n")
    
    while True:
        age_input = input("Please enter your age to play: ").strip()
        
        # Check if input is a valid number
        if age_input.isdigit():
            age = int(age_input)
            if age >= 12:
                print(f"🎉 Awesome! {age} is a great age for this challenge. Let's begin!\n")
                break
            elif age < 0:
                print("Time travel isn't real yet! Please enter a valid age.")
            else:
                print("Sorry, you need to be at least 12 years old to play this quiz. Goodbye!")
                return
        else:
            print("❌ Invalid input. Please enter a whole number for your age.")
            
    time.sleep(1)

    # 2. Quiz Questions (Exactly 5 Questions)
    quiz_data = [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the largest mammal on Earth?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Megalodon"],
            "answer": "B"
        },
        {
            "question": "How many bones are in an adult human body?",
            "options": ["A. 106", "B. 206", "C. 306", "D. 406"],
            "answer": "B"
        },
        {
            "question": "Which country is home to the kangaroo?",
            "options": ["A. South Africa", "B. Austria", "C. Australia", "D. Brazil"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. CO2", "B. H2O", "C. O2", "D. NaCl"],
            "answer": "B"
        }
    ]

    score = 0
    
    # 3. The 5-Time Loop
    for i in range(5):
        q = quiz_data[i]
        print(f"Question {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
    
        # Input validation loop
        while True:
            guess = input("Your answer (A, B, C, or D): ").strip().upper()
            if guess in ["A", "B", "C", "D"]:
                break
            print("Invalid choice. Please enter A, B, C, or D.")

        # Check answer
        if guess == q['answer']:
            print("✨ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {q['answer']}.\n")
        
        time.sleep(0.5)

    # Final Score
    print("--- QUIZ OVER ---")
    print(f"Your Final Score: {score}/5")
    if score == 5:
        print("🏆 Perfect! You're a trivia genius!")
    elif score >= 3:
        print("👍 Good job! Solid performance.")
    else:
        print("📚 Better luck next time!")

# Run the game
if __name__ == "__main__":
    run_quiz()