import time

print("Welcome to Hangman!\nPro tip...The other player(s) should not see the word")
secret_word = input("Type the word that is to be guessed: ").lower()

print("Game begins in a few :)")
time.sleep(2)
length = len(secret_word)
print(f"Your word has {length} words")

output = []
for letter in secret_word:
    output += "_"
print(output)

trials = 0
while True:
    guess = input("Guess a letter: ").lower()

    for position in range(length):
        letter = secret_word[position]
        if letter == guess:
            output[position] = letter
    print(output)
    trials += 1

    if "_" not in output:
        print(f"You have won and finished with {trials} trials!")
        break