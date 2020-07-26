# Constants (Update these to be the correct numbers)
TAX = 7.2
PEOPLE_THRESHOLD = 5
LARGE_PARTY_TIP = 20
SMALL_PARTY_TIP = 15

def get_meal_cost():
    meal_cost = float(input ("Please enter your meal cost: "))
    return meal_cost

def get_party_number():
    return int (input ("Please enter the number of people in your party: "))

def calculate_meal_total():
    """
    This program calculates how much your meal costs including
    tax and tip. The tip is based on the number of people in
    your party.
    """
    cont = 'Y'
    while cont == 'Y' or cont == 'y' or cont == 'Yes' or cont == 'yes' or cont == 'YES':

        meal_cost = get_meal_cost()

        meal_tax = meal_cost * TAX/100
        num_people = get_party_number()

        if num_people < PEOPLE_THRESHOLD:
            tip = meal_cost * SMALL_PARTY_TIP/100
        else:
            tip = meal_cost * LARGE_PARTY_TIP/100

        total_cost = meal_cost + tip + meal_tax

        print('Your meal cost is ', meal_cost)
        print('Tip = ', format(tip, '.1f'), ' and ', 'tax =', format(meal_tax, '.2f'))
        print('Your total cost is ', format(total_cost, ',.2f'))
        cont = input ("Do you want to cont? (enter Y ")


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    calculate_meal_total()