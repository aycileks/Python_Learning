# GlobalAIHub Python Introduction Homework3

name = str(input("What is your name? : "))
print("\nHello {}!".format(name) + " Let's build a dictionary first for the Hangman!")
count = int(input("\nHow many words would like to enter into the dictionary? : "))

n = 1
dictionary = []
while n <= count:
    dictionary.append(str(input("Please enter the word {} : ".format(n))))
    n += 1
print("\nOur dictionary is ready, let's start the game!")

import random as rnd


def randomWord(dictionary):
    index = rnd.randint(0, len(dictionary) - 1)
    return dictionary[index]


word = randomWord(dictionary)
cnt = int(len(word))
guess = str()
check = []
ordered_word = sorted(word)
ordered_guess = str()

print("\nThe secret word is composed of {} letters.".format(cnt))

for i in word:
    print("_", end=" ")

print("\n")
print(
    "You are given 7 chances to predict the correct letters inside the secret word!\n"
)

chan = 1
while chan <= 7:
    print(f">>> Chance {chan} <<<")
    letter = str(input("\nPlease enter a letter :"))
    if letter in check:
        print(f"You have already entered '{letter}'. Please try again...")

    elif letter in word and letter != "":
        print("\nCongrats!")
        guess = guess + letter
        ordered_guess = sorted(guess)
        check.append(letter)
        print(ordered_guess)
        print(ordered_word)
        if ordered_guess == ordered_word:
            print("\nYou won! The secret word was :" + word)
            exit(0)
    else:
        chan += 1
        print("\nSorry, wrong guess...")
        check.append(letter)

print("\nYou lost! The secret word was : " + word)
