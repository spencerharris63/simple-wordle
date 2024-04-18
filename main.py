import random


def load_words(file="words.txt"):
    with open(file, 'r') as file_handle:
        words = [line.strip().lower() for line in file_handle if len(line.strip()) == 5]
    return words


def check_guess(guess, correct_word):
    result = ["_"] * len(correct_word)
    correct_word_count = {}
    for letter in correct_word:
        correct_word_count[letter] = correct_word_count.get(letter, 0) + 1

    # First pass: mark correct positions
    for i in range(len(guess)):
        if guess[i] == correct_word[i]:
            result[i] = guess[i].upper()
            correct_word_count[guess[i]] -= 1

    # Second pass: mark letters in the word but in the wrong position
    for i in range(len(guess)):
        if guess[i] != correct_word[i] and guess[i] in correct_word_count and correct_word_count[guess[i]] > 0:
            result[i] = guess[i].lower()
            correct_word_count[guess[i]] -= 1

    return ' '.join(result)


def main():
    words = load_words()
    correct_word = random.choice(words)
    attempts = 6
    current_guess = "_" * 5
    while attempts > 0:
        print(current_guess)
        guess = input("Enter your guess: ").lower()
        if len(guess) != 5:
            print("Invalid guess. Please enter a valid five-letter word.")
            continue  # Skip the rest of the loop and go back to asking for a guess
        if guess == correct_word:
            print("YOU WIN")
            print(' '.join(letter.upper() for letter in correct_word[:5]))
            return
        current_guess = check_guess(guess, correct_word)
        attempts -= 1
        print(f"Remaining attempts: {attempts}")

    print("YOU LOSE")
    print(f"The correct word was {correct_word}")


if __name__ == "__main__":
    main()
