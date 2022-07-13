import random

def select_option():
    print("Please select an option:")
    print("1) Create a random character")
    print("2) Exit")
    userinput = int(input())  # TODO: Entering non int crashes.
    if userinput not in range(1, 3):
        print('Sorry! that is not an option')
        select_option()
    if userinput == 1:
        random_character()
        again = input('Another character?\n 1)Yes \n 2)No \n')
        if again == '1':
            random_character()
        else:
            select_option()
    if userinput == '2':
        print("Bye!")
        exit()


def random_race():
    # TODO: Add Dragonborn and Elf sub races!
    race_int = random.randint(0, 9)
    # print(race_int)
    races = ['Elf', 'Human', 'Half-Orc', 'Half-Elf', 'Tiefling', 'Dwarf', 'Warforged', 'Dragonborn', 'Halfling',
             'Gnome']
    race = races[race_int]
    return race


def random_gender():
    gender_int = random.randint(0, 10)
    # print(gender_int)
    if gender_int == 10:
        return 'Non-binary'
    elif gender_int in range(0,5):
        return 'Male'
    elif gender_int in range(5,10):
        return 'Female'


def random_personality():
    personalities = ['Helpful', 'Withdrawn', 'Egotistical', 'Eccentric', 'Pious', 'Shady', 'Rude', 'Sloppy', 'Kind',
                     'Responsible']
    personality_int = random.randint(0, 9)
    personality = personalities[personality_int]
    return personality


def random_age(race):
    if race == 'Elf':
        age = random.randint(100, 350)
    else:
        age = random.randint(18, 100)
    return str(age)


def random_character():
    race = random_race()
    age = random_age(race)
    gender = random_gender()
    personality = random_personality()
    print('Your random character is: \n', 'Age:', age, '\n Gender:', gender,
          '\n Race:', race, '\n Personality:', personality)


if __name__ == '__main__':
    print("Welcome to the DnD generator!")
    select_option()
