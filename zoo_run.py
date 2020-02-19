from zoo_classes import *
from zoo_current_animals import *
from zoo_functions import *
animal_list = [Donald, Boris, Nev, Piers]
location_list = ['Zone1 - Animals', 'Zone2 - Reptiles', 'Zone3 - Fish', 'Zone4 - Amphibians', 'Zone5 - Birds']


while True:
    print('Choose a number from the following options:'
          '\n 1: List animals at Sams zoo '
          '\n 2: List locations of animals '
          '\n 3: Add new animal to the zoo ')

    user_input = input('Whats your option ')

    if user_input.strip() == '1':
        for i in animal_list:
            print(f'I am {i.name} the {i.species} and I am {i.character[0]}')

    elif user_input.strip() == '2':
        for i in location_list:
            print(i)

    elif user_input.strip() == '3':
        name = input('Whats the name of the animal? ')
        print('What class does the animal belong to?  '
              '\n1 -- Mammal'
              '\n2 -- Bird'
              '\n3 -- Fish'
              '\n4 -- Reptile'
              '\n5 -- Amphibian')
        classes = input('What class does the animal belong to?  ')
        if classes.strip() == '1':
            species = species_question()
            new = Mammal(name, species)
            new.add_character(character_question())
            animal_list.append(new)
            thank_you()
        elif classes.strip() == '2':
            species = species_question()
            new = Bird(name, species)
            new.add_character(character_question())
            animal_list.append(new)
            thank_you()
        elif classes.strip() == '3':
            species = species_question()
            new = Fish(name, species)
            new.add_character(character_question())
            animal_list.append(new)
            thank_you()
        elif classes.strip() == '4':
            species = species_question()
            new = Reptile(name, species)
            new.add_character(character_question())
            animal_list.append(new)
            thank_you()
        elif classes.strip() == '5':
            species = species_question()
            new = Amphibian(name, species)
            new.add_character(character_question())
            animal_list.append(new)
            thank_you()

        # species = input('What is their species? ')
        # character = input('Do they have any distinguishable characteristics? ')

        # animal = classes.strip(name, species)
        # animal_list.append(animal)
