# Constants (Update these to be the correct numbers)
TAX = 0.0725
PEOPLE_THRESHOLD = 5
LARGE_PARTY_TIP = 0.20
SMALL_PARTY_TIP = 0.15


def get_tip(total_cost, num_people):
    """
    Returns the tip given the `total_cost` of a meal
    and the number of people who ate. Larger parties
    pay a larger tip.
    """
    if num_people > PEOPLE_THRESHOLD:
        return total_cost * LARGE_PARTY_TIP
    else:
        return total_cost * SMALL_PARTY_TIP


def get_tax(total_cost):
    """
    Returns tax given the `total_cost` of a meal
    """
    return total_cost * TAX


def calculate_total(total_cost, num_people):
    """
    Given the total_cost of a meal and the number of
    people who ate, returns the total for the meal
    including tax and tip.
    """
    tip = get_tip(total_cost, num_people)
    tax = get_tax(total_cost)
    return total_cost + tip + tax


def calculate_meal_total():
    """
    This program calculates how much your meal costs including
    tax and tip. The tip is based on the number of people in
    your party.
    """
    print(calculate_total(25.30, 6))
    print(calculate_total(36.30, 4))


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    calculate_meal_total()