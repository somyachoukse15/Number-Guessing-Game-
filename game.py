import random

def play_game():
    secret_number = random.randint(1, 20)
    attempts = 5

    print("I have chosen a number between 1 and 20. Can you guess it?")
    print("---------------------------------------------------")

    for i in range(attempts):
        print(f"\nAttempt {i + 1} of {attempts}")
        
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid integer!")
            continue
            
        if guess == secret_number:
            print(f"🎉 You won!! You guessed the correct number in {i + 1} attempts!")
            return
        elif guess < secret_number:
            print("📉 Too Low")
        else:
            print("📈 Too High")
            
    print(f"\n😢 Ohh you lost... The secret number was {secret_number}.")

play_game()
