def sum_squares_input(num1, num2):
    """
    This function takes two values and return sum of sqaures
    :param num1:
    :param num2:
    :return:
    """
    return (num1**2 + num2**2)

def print_sum_squares_input():
    result = 0
    num1 = int(input ("Enter int first number: "))
    num2 = int(input("Enter int second number: "))
    sum_squares_input(num1, num2)


def main():
    print_sum_squares_input()

main()