# a simple high low number guessing game.
#
class too_high_too_low:
    def __init__(self):
        # setup self.number to be a random number from 1 to 100
        # self.guesses to be zero
        pass

    def play(self):
        while True:
            pass
            # Get a number guess from the user (between 1 and 100)
            # Convert the input to an integer
            # Increment the number of guesses by 1
            # Check *if* the guess equals the secret number
            # If correct, print a congratulations message with the number of guesses
            # Exit the loop
            # Check *if* the guess is less than the secret number
            # If so, print "Too low!"
            # Otherwise (the guess must be too high)
            # Print "Too high!"
            # Check *if* the player has made 10 guesses
            # If so, print a message saying they've run out of guesses and reveal the number
            # Exit the loop


def main():
    game = too_high_too_low()
    game.play()


if __name__ == "__main__":
    main()
