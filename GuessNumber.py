import random
secret_number = random.randint(1,10)
for guesses in range(1,6):
    print("Enter Your Guessed Number")
    guessed_int = int(input())
    if guessed_int > secret_number:
        print("You Guessed Too High")
    elif guessed_int < secret_number:
        print("Your Guessed Too Low")
    else:
        break
if guessed_int == secret_number:
    print(f"Good Job... You made it right in {guesses}  guesses") 
else:
    print("You are not a good Guesser")