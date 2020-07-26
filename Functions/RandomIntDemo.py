import random

def create_random_int():
    number = random.randint(1,1)
    number = random.randrange(3)
    number = random.randrange(3, 6)
    number = random.random()
    number = random.uniform(0.0, 1.2)
    print(number)

if __name__ == "__main__":
    create_random_int()