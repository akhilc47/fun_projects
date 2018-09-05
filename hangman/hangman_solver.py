import random
import time
from collections import defaultdict

t1 = time.time()
with open('dict.txt', 'r') as df:
    dictionary = []
    for word in df:
        dictionary.append(word[:-1])
backup = dictionary
correct = 0
incorrect = 0
total = 1000
for i in range(total):
    dictionary = backup
    hangman_word = random.choice(dictionary)
    # hangman_word = dictionary[i]
    word_length = len(hangman_word)
    display_word = ['_']*word_length
    # print(hangman_word, word_length)
    dictionary = [w for w in dictionary if len(w) == word_length]
    tried_letters = []
    correct_letters = []
    incorrect_letters = []

    solved = False
    failed = False
    tries = 0
    while not solved and not failed:
        # print('\n\n', ' '.join(display_word))
        # print('number of possible words:', len(dictionary))
        # print('tries: {}, correct: {}, incorrect: {}'.format(tries, correct_letters, incorrect_letters))
        #  Find the letter which is most used in dictionary. Appearance of a letter is counted only once per word.
        frequency = defaultdict(lambda: 0)
        for word in dictionary:
            for letter in set(word):
                if letter not in tried_letters:
                    frequency[letter] += 1
        probable_letter = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[0][0]
        tried_letters.append(probable_letter)
        if probable_letter in hangman_word:
            correct_letters.append(probable_letter)
            dictionary = [w for w in dictionary if probable_letter in w]
            positions = [pos for pos, val in enumerate(hangman_word) if val == probable_letter]
            for pos in positions:
                display_word[pos] = probable_letter
            new_dict = []
            for word in dictionary:
                if positions == [pos for pos, val in enumerate(word) if val == probable_letter]:
                    new_dict.append(word)
            dictionary = new_dict
        else:
            incorrect_letters.append(probable_letter)
            dictionary = [w for w in dictionary if probable_letter not in w]
            tries += 1
        if tries == 5:
            failed = True
        if '_' not in display_word:
            solved = True
    if solved:
        # print('\n\nYou solved it in {} tries, word: {}'.format(tries, ''.join(display_word)))
        correct += 1
    elif failed:
        # print('\n\nYou ran out of tries, the word was:', hangman_word)
        incorrect += 1
    else:
        print('\n\nSomething broke?!')

print('correct: {}, incorrect: {}, total: {}, success rate: {}%, time taken: {} seconds'
      .format(correct, incorrect, total, correct/total*100, time.time()-t1))
