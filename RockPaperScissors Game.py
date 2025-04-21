# Rock Paper Scissors Game in python
# Made by Kath Fillman circa 2023

import random
leaderboard = {}

def startup():
    # Intro text & directions
    print('Welcome to the ULTIMATE rock-paper-scissors showdown')
    print('This is a best out of 5 scoring system. Your move options are: rock, paper, or scissors')
    print ('1. Play the game')
    print('2. View rules')
    print('3. something else not yet programed')
    choice = input('Input the number of your choice: ')
    # if-else statements for text input
    if choice=='1':
        play_game()
    elif choice=='2':
        print()
        print()
        print()
        print('Rock-Paper-Scissors is a classic game using hand signals that resemble rocks, scissors, and paper')
        print('Commonly played by school children, the rules are simple:')
        print('Paper covers rock, rock smashes scissors, and scissors cuts paper')
        print("Each of these options are called a 'throw' as you typically 'throw' these hand symbols while playing")
        print('In this program, it is scored on a best-out-of-five system')
        print()
        input("Press enter to return to the main title page")
        print()
        print()
        print()
        startup()
    elif choice=='3':
        print()
        print("oops! you've stubled into a construction zone. This will eventually be a leaderboard- Check back soon.")
        print('Returning you to main screen...')
        print()
        startup()
    else:
        choice= input('The input was not recognized. Please try again: ')

def play_game():

    # Used to check that player has valid input and is list of computer throws
    throws = ['rock', 'paper', 'scissors']
    # Used for scoring. keys are the throw and values are what looses to it
    scoring_key = {'paper':'rock', 'rock':'scissors', 'scissors':'paper'}
    player_score = 0
    computer_score = 0
    computer_throws=[]
    i=0 #round number
    k=0

    # Player name intake. Will be used for leaderboard.
    global name
    try:
        print('Welcome back', name)
    except:
        name=input('Who is playing? ')

    # Generates computer's throws
    for k in range (0,5):
        choice = random.choice(throws)
        computer_throws.append(choice)
    
    # Begin player input of game using if statements
    while i<5:
        print()
        throw = input('This is round number {}. What will you throw: '.format(i+1))
        if throw.casefold() in throws: #makes sure input is valid and makes it case insensitive
            print('You chose {} and the computer chose {}.'.format(throw, computer_throws[i]))
            if throw == computer_throws[i]: #if tie
                print('Both you and the computer have chosen {}! This round is a tie.'.format(throw))
                i=i+1 #increases round count
            elif scoring_key.get(throw)==computer_throws[i]: # if player win
                player_score=player_score+1 #adds win to player score
                print('You win this round! Score: {}'.format(player_score))
                i=i+1 #increases round count
            else: # if computer win
                computer_score=computer_score+1
                print('Computer wins this round. Score: {}'.format(player_score))
                i=i+1 #increases round count
        else:
            print('Please enter a valid throw. Your options are rock, paper, or scissors.')
            continue
    print()
    if player_score>3: #if player wins
        print()
        print('The final score is {}:{}- player wins!'.format(player_score, computer_score))
        print("Congratulations, {}, you've won!".format(name))
    elif player_score==computer_score: # if tie
        print()
        print("The final score is {}:{}- it's a tie!".format(player_score, computer_score))
    else: # if player looses
        print()
        print('The final score is {}:{}- computer wins!'.format(player_score, computer_score))
        print('Good try, {}, but you lost this time.'.format(name))
    input('Click enter to continue') 
    print()

    # Choice to return to menu/play again
    print("Would you like to:")
    print('1. Return to the main menu')
    print('2. Play again')
    choice = input('Enter the number of your choice:')
    if choice=='1':
        print()
        print()
        print()
        startup()
    if choice=='2':
        print()
        print()
        print()
        play_game()


startup()