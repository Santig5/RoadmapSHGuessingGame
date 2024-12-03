import random

def guessingGame():
    print('\
Please Select Difficulty Level: \n \
1. Easy (10 Guesses)\n \
2. Medium (5 Guesses)\n \
3. Hard (3 Guesses)')

    difficultyLevel = int(input())
    if difficultyLevel == 1:
       guesses = 10
    elif difficultyLevel == 2:
        guesses = 5
    else: 
        guesses = 3

    answer = random.randint(1,100)
    print('I am thinking of a number between 1 and 100')
    counter = 0
    while counter < guesses:

        print('Take a guess')
        counter = counter + 1
        guess = int(input())
        if guess == answer:
            print('Congratulations! You guessed my number in ' + str(counter) + ' guesses.')
            break
        elif guess < answer:
            print('Your guess is too low.')
        elif guess > answer:
            print('Your guess is too high.')

    if counter == guesses + 1:
        print('Oh no! the answer was ' + str(answer) + '. Better luck next time!')
        
    print('Do you want to play again? (y/n)')
    playAgain = input()
    if playAgain == 'y':
        guessingGame()
    else:
        exit
        
guessingGame()
