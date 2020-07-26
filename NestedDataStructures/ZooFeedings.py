"""
Author Ayca Tuzmen
Adopted from CS106AP Summer 2019 by Sonja Johnson-Yu
22.04.2010
"""


def get_full_animal_dict(filename):
    """
    Returns a dict of animal names (not including the bears) containing
    a dict containing the animal type, diet, and list of times fed.

    Input:
        filename (string): file of zoo animals

    Return:
        animal_feedings (dict): animal names to full animal info
    """
    animals = {}
    with open (filename, 'r') as f:
        for line in f:
            line = line.strip()
            split_line = line.split(',')
            animal_info = {}
            animal_info['type'] = split_line[1]
            animal_info['diet'] = split_line[2]
            animal_info['times'] = split_line[3:]
            animals[split_line[0]] = animal_info
    return animals

def get_feeding_times_dict(filename):
    """
    Returns a dict of animal names (not including the bears) containing
    a list of the times each animal has been fed.

    Input:
        filename (string): file of zoo animals

    Return:
        animal_feedings (dict): animal names to list of feeding times
    """
    animal_feedings = {}
    with open (filename, 'r') as f:
        for line in f:
            line = line.strip()
            split_line = line.split(',')
            if split_line[1] == 'bear':
                continue
            animal_feedings[split_line[0]] = split_line[3:]
    return animal_feedings



def get_animal_feedings_dict(filename):
    """
    Returns a dict of animals (not including the bears) and
    corresponding number of times the animals have been fed.

    Input:
        filename (string): file of zoo animals

    Return:
        animal_feedings (dict): animal names to num feedings
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
    # print_animals_feedings('zoo.txt')
    # first iteration, just animal - num times fed
    # print('Printing simple animal to # times fed dict:')
    # print(get_animal_feedings_dict('zoo.txt'))
    # second iteration, animal - list of times fed
    # print('Printing animal to list of times fed dict:')
    # print(get_feeding_times_dict('zoo.txt'))
    # # third iteration, animal - all info
    # print('Printing animal to full info dict:')
    # print(get_full_animal_dict('zoo.txt'))
    str = input("enter the name of a animal ")
    while str:

        animals = get_full_animal_dict('zoo.txt')
        if str in animals.keys():
            new_diet = input('enter the new diet ')
            animals[str]['diet'] = new_diet
            new_times = input('enter the new times ')
            new_times_list = new_times.split(',')
            animals[str]['times'] = new_times_list
            print(animals)
        else:
            print('No such animal in the zoo')
        str = input("enter the name of a animal ")


if __name__ == '__main__':
    main()