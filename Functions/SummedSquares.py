
def sum_squares(a, b):
    """
    Takes in two values and returns the sum of their squares.

    Input:
        a (int): first value
        b (int): second value
    Returns:
        summed_squares (int): sum of squares
    """
    return a * a + b * b


def main():
    """Runs summed squares function"""
    print(sum_squares(5, 6))


if __name__ == '__main__':
    main()