# Madlib Generator

# Intro & get words
print("Welcome to MadLibs! Please enter the following words to create your silly story!")
animal1=input('An animal: ')
animal2=input('Another animal: ')
name=input('A name: ')
food=input('A food: ')
adjetive= input('An adjetive: ')
noun= input('A noun: ')

# Stories
story1 ="There once was a {} named {}, who lived in a house made of {}! This house was not very {}, but was very tastey for the {} that lived around {}. When they eventally ate through {}'s home, they built {} a new one out of {}.".format(animal1, name, food, adjetive, animal2, name, name, name, noun)

# Print story
print(story1)
