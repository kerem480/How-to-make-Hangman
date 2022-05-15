import random

print("Welcome to hangman")

name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['computer', 'science', 'programming','keep','start','sing'
        'python', 'mathematics', 'player', 'condition','espacially',
        'water','board', 'geeks','score','forward','mouse','screen']

word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            print(char, end=" ")

            failed += 1

    if failed == 0:

        print("You Win")

        print("The word is: ", word)
        break

    print()

    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1

        print("Wrong")

        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Dead")

