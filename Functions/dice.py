# This program simulates the rolling of dice.
import random

# Constants for the minimum and maximum random numbers
MIN = 1
MAX = 6

def main():
    # Simulate rolling the dice.

    print('Rolling the dice...')
    print('Their values are:')
    print(random.randint(MIN, MAX))
    print(random.randint(MIN, MAX))


# Call the main function.
main()
