import random

words = ["apple", "banana", "kiwi", "car", "funny", "pie"]
chosen_word = random.choice(words)
hidden_word = ["_"] * len(chosen_word)
wrong_letters = []
tries = 10

print("Plan hangman")
print()
print(" ".join(hidden_word))
print()

while "_" in hidden_word:

    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for i in range(len(hidden_word)):
            if chosen_word[i] == guess:
                hidden_word[i] = guess
                print()
                print(hidden_word)
                print(f"You have {tries} tries left")
                print(f"Letters not in word: {wrong_letters}")


    elif guess not in chosen_word:
        print(hidden_word)
        print()
        print("That letter is not in the word")
        tries -= 1
        print()
        print(f"You have {tries} tries left")
        wrong_letters.append(guess)
        print()
        print(f"Letters not in word: {wrong_letters}")

    if tries == 0:
        print(f"You lose, the word was {chosen_word}")
        break

if not "_" in hidden_word:
    print()
    print("Congrats, you guessed the correct word")
