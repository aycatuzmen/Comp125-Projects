# Constants (Update these to be the correct numbers)
TAX = 0.0725
THRESHOLD = 5
LARGE_PARTY_TIP = 0.20
SMALL_PARTY_TIP = 0.15

def get_tip_return(total_cost, num_people):
    if num_people > THRESHOLD:
        return total_cost * LARGE_PARTY_TIP
    return total_cost * SMALL_PARTY_TIP

def get_tip_print (total_cost, num_people):

    if num_people > THRESHOLD:
        print (total_cost * LARGE_PARTY_TIP)
    print( total_cost * SMALL_PARTY_TIP)

def main():
    tip = format(get_tip_return(26.50, 6), '.2f')
    print('Tip = ', tip)

main()