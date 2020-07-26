# Constants
TAX = 0.0725
PEOPLE_THRESHOLD = 5
LARGE_PARTY_TIP = 0.20
SMALL_PARTY_TIP = 0.15


def calculate_meal_total():
    """
    This program calculates how much your meal costs including
    tax and tip. The tip is based on the number of people in
    your party.
    """
    total_cost = 50
    num_people = 4
    tax = total_cost * TAX

    # Calculate tip based on num_people
    if num_people > PEOPLE_THRESHOLD:
        tip = total_cost * LARGE_PARTY_TIP
    else:
        tip = total_cost * SMALL_PARTY_TIP

    # Calculate and print the total
    total = total_cost + tax + tip
    print(total)


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    calculate_meal_total()