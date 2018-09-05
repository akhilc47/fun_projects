import random


word = random.choice(open('dict.txt', 'r').readlines())[:-1]
print(word, len(word))
word_length = len(word)
display_word = ['_ ']*word_length
tried_letters = []
incorrect_letters = []

solved = False
failed = False
while not solved and not failed:
    print('\n\n')
    print(''.join(display_word))
    print('\n')
    print('Incorrect letters: ', incorrect_letters)
    letter = ''
    while not letter.isalpha():  # Prompt till an alphabet is obtained
        letter = input('Try a letter: ')[0]  # Consider first char, if user entered multiple chars
    tried_letters.append(letter)
    if letter not in word:
        incorrect_letters.append(letter)
        if len(incorrect_letters) == 6:
            failed = True
        continue
    for i in range(word_length):
        if display_word[i] == '_ ' and word[i] == letter:
            display_word[i] = letter
    if '_ ' not in display_word:
        solved = True

if solved:
    print('You solved the puzzle. The word was %s' % word)
elif failed:
    print('You ran out of tries. The word was %s' % word)
else:
    print('Something bad happened. Please call 911')
