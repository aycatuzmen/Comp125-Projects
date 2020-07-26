"""
CS106AP Summer 2019
Written by Sonja Johnson-Yu
7.15.19
"""

def print_animals_feedings(filename):
    """
    Prints list of zoo animals (not including the bears) and
    corresponding list of number of times the animals have
    been fed.

    Input:
        filename (string): file of zoo animals
    """
    animals = []
    num_feedings = []
    with open(filename, 'r') as f:
        for line in f:
            split_line = line.split(',')
            if split_line[1] == 'bear':
                continue
            animals.append(split_line[0])
            num_feedings.append(len(split_line[3:]))

    print(animals, num_feedings)


def get_animal_feedings_dict(filename):
    """
    Returns a dict of animals (not including the bears) and
    corresponding number of times the animals have been fed.

    Input:
        filename (string): file of zoo animals

    Return:
        animal_feedings (dict): animal names to
    """
    animal_feedings = {}
    with open(filename, 'r') as f:
        for line in f:
            split_line = line.split(',')
            if split_line[1] == 'bear':
                continue
            animal_feedings[split_line[0]] = len(split_line[3:])

    return animal_feedings


def main():
    print_animals_feedings('zoo.txt')
    #print(get_animal_feedings_dict('zoo.txt'))



if __name__ == '__main__':
    main()