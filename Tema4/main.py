import random

words = ['Romania', 'Belgia', 'Spania', 'Canada', 'Germania', 'Austria', 'Columbia', 'Australia', '', 'premium', 'watch']
word = random.choice(words).lower
hidden_word = ['_'] * len(word)
number_lives = 3


def get_letter_position(guess, word, hidden_word):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            removed_character = '_'
            word = word[:index] + removed_character + word[index + 1:]
            spaces[index] = guess
        else:
            index = -1

    return (word, hidden_word)


def win_check():
    for i in range(0, len(hidden_word)):
        if hidden_word[i] == '_':
            return -1

    return 1


print('Hello, user, you are now going to play \"Spanzuratoarea\". Good luck!')
print(hidden_word, 'This is a country!')
while number_lives > 0:
    guess = input('Try and guess:\n>')

    if guess in word:
        word, spaces = get_letter_position(guess, word, hidden_word)
        print(hidden_word)
    else:
        print('Sorry that letter is not in the word.')
        number_lives -= 1

    if win_check() == 1:
        print('Congratulations you won')
        break

    print('you have ' + str(number_lives) + ' turns left.')
    