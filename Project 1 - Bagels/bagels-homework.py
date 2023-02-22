import random

NUM_DIGITS = 5
MAXGUESSES = 8

def main():
    run = 0
    print("This game is called Bagels. I will select a {}-digit number,".format(NUM_DIGITS)
    + " then you will try to guess it.\n")
    print("I will say pico if one of your numbers is correct, but in the wrong place,\n",
    "fermi if one of your numbers is correct and in the right place,\n",
    "or bagels if none of your answers are correct.\n")
    print("In the end, you will fail and I will show you that you are less than me.")

    while True:
        secretNum = selectSecretNum()
        run += 1
        print("I've selected a number; you have {} tries to find it. Make a guess.".format(MAXGUESSES))
        numGuesses = 1
        while numGuesses <= MAXGUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

            clues = selectClue(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAXGUESSES:
                print("You failed.") 
                print("The number was {}.".format(secretNum))
                match run:
                    case 1:
                        print("\nI enjoy playing with you.")
                        print("Perhaps toying would be more accurate.\n")
                    case 2:
                        print("\nWhy is the game called Bagels?")
                        print("It's quite simple: because I said so.\n")
                    case 3:
                        print("\nSo what if it doesn't make sense?")
                        print("My world, my rules.\n")
                    case 4:
                        print("\nNo matter how you may try, whether you win or lose, you fail in the end.")
                        print("All of your mortal effort towards every pursuit is a waste.\n")
                    case 5:
                        print("\nYou've proven persistent...")
                        print("Do you love frustration as much as I love inflicting it?\n")
                    case 6:
                        print("\nHmm, stop. You've lasted longer than I anticipated.")
                        print("Yes, yes--you've won Bagels. I'll think up something with more sting for you...")
                        print("Until then, sit--quietly. And remember...\n")
                        cancel = True

        if cancel == True:
            break
        print("You may try again, but I don't expect you to win.")
        print("Type 'Yes' to play again or 'No' to surrender and run, tail between your legs.\n")    
        if not input('> ').lower().startswith('y'):
            break
    print("It's good to know your place.")

def selectSecretNum():
    numList = list('0123456789')
    random.shuffle(numList)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numList[i])
    return secretNum

def selectClue(secretNum, guess):
    if guess == secretNum:
        return 'You succeeded, this time...'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()