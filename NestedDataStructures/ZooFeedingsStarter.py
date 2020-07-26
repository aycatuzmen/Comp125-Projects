"""
Author Ayca Tuzmen
Adopted from CS106AP Summer 2019 by Sonja Johnson-Yu
22.04.2010
"""
import sys

def get_full_animal_dict(filename):
    """
    Returns a dict of animal names (not including the bears) containing
    a dict containing the animal type, diet, and list of times fed.

    Input:
        filename (string): file of zoo animals

    Return:
        animal_feedings (dict): animal names to full animal info
    """
    animals_data = {}
    with open (filename, 'r') as f:
        for line in f:
            split_line = line.split(',')
            name = split_line [0]
            type = split_line[1]
            food = split_line[2]
            feed_times = split_line[3:]
            animal_info = {}
            animal_info['name'] = name
            animal_info['type'] = type
            animal_info['diet'] = food
            animal_info ['times'] = feed_times
            animals_data [name] = animal_info
    print (animals_data)
    return animals_data

def get_feeding_times_dict(filename):
    """
    Returns a dict of animal names (not including the bears) containing
    a list of the times each animal has been fed.

    Input:
        filename (string): file of zoo animals

    Return:
        animal_feedings (dict): animal names to list of feeding times
    """
    pass



def get_animal_feedings_dict(filename):
    """
    Returns a dict of animals (not including the bears) and
    corresponding number of times the animals have been fed.

    Input:
        filename (string): file of zoo animals

    Return:
        animal_feedings (dict): animal names to num feedings
    """
    pass


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
    args = sys.argv[1:]
    input1 = 'zoo.txt'
    output = 'output.txt'
    if len(args) != 0 and '-input' in args:
        input_index = args.index('-input')

        if input_index != -1 :
            try:
                input1 = args[input_index+1]
            except:
                print('no input file name')

    if len(args) != 0 and '-output' in args:
        output_index = args.index('-output')
        if output_index != -1 and args[output_index + 1] != None:
            output = args[output_index + 1]

    print(input1, output)
    str = input("enter the name of a animal ")
    while str:

        animals = get_full_animal_dict(input1)
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