""" Udacity """

flower_dict = {}


def flower_read():
    with open('flowers.txt', 'r') as f:
        for line in f:
            letter, flower = line.split(":")
            flower_dict[letter] = flower.strip()


def user_input(f_dict):
    try:
        name = input("Enter your First [Space] Last name only: ")
    except ValueError:
        print("Not valid input.")

    word = f_dict[name.title()[0]]
    print("Unique flower name with the first letter: ", word)


flower_read()
user_input(flower_dict)
