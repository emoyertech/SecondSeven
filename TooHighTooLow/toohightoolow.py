# a simple high low number guessing game.
#
import random
class too_high_too_low:
    
    

    def __init__(self):
        # setup self.number to be a random number from 1 to 100
        self.number = random.randint(1, 100)
        # self.guesses to be zero
        self.guesses = 0
        pass

    def play(self):
        while True:
            self = random.randint(1, 100)
            attempts = 0
    def play(self):
        previous_guess = None # Initialize so it exists for the first check
        
        while True:
            # Removed: self = random.randint (This was breaking your class)
            try:
                guess = int(input("Guess a number between 1 and 100: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue # Skip to next iteration to ask again

            self.guesses += 1

            # Duplicate Guess Check
            if guess == previous_guess:
                print("You've already guessed that number! Try a different one.")
                self.guesses -= 1 
            else:
                previous_guess = guess 

            # Logic Checks
            if guess < self.number:
                print("Too low!")
            elif guess > self.number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number in {self.guesses} guesses!")
                break

            # Hints and Game Over
            if self.guesses == 3:
                print("Hint: The number is " + ("a multiple of 5." if self.number % 5 == 0 else "not a multiple of 5."))
            if self.guesses == 5:
                print("Hint: The number is " + ("even." if self.number % 2 == 0 else "odd."))
            if self.guesses == 8:
                print("Hint: The number is " + ("greater than 50." if self.number > 50 else "less than or equal to 50."))

            if self.guesses >= 10:
                print(f"Game over! You've run out of guesses. The number was {self.number}.")
                break

def display_scoreboard(previous_guess):
    print(f"Previous guess: {previous_guess}")

def main():
    game = too_high_too_low()
    game.play()


if __name__ == "__main__":
    main()
