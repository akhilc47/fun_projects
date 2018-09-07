import math
import os
import random
import time
from collections import defaultdict
from multiprocessing import Process, Manager

t1 = time.time()

sorted_dictionary = defaultdict(lambda: [])
listed_dictionary = []
with open('reduced_dict.txt', 'r') as df:
    for word in df:
        sorted_dictionary[len(word)-1].append(word[:-1])
        listed_dictionary.append(word[:-1])
dict_size = len(listed_dictionary)


def run_solver(total, proc_id, result):
    correct = 0
    incorrect = 0
    with open(str(proc_id)+'.txt', 'w') as fout:
        for i in range(proc_id*math.ceil(dict_size/4), min((proc_id+1)*math.ceil(dict_size/4), dict_size)):
            hangman_word = listed_dictionary[i]
            word_length = len(hangman_word)
            display_word = ['.']*word_length
            dictionary = sorted_dictionary[word_length]
            tried_letters = []
            correct_letters = []
            incorrect_letters = []

            solved = False
            failed = False
            while not solved and not failed:
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

                if '.' not in display_word:
                    solved = True
                    correct += 1
                elif len(incorrect_letters) == 6:
                    failed = True
                    incorrect += 1
                    fout.write(hangman_word+'\n')

    result[proc_id] = incorrect
    print(result)
    print('correct: {}, incorrect: {}, total: {}, success rate: {}%, time taken: {} seconds'
          .format(correct, incorrect, correct+incorrect, correct/(correct+incorrect)*100, time.time()-t1))


if __name__ == '__main__':
    total = dict_size  # input multiple of CPU count
    processes = []
    result = Manager().list([0]*os.cpu_count())

    for proc_id in range(os.cpu_count()):
        processes.append(Process(target=run_solver, args=(int(total/os.cpu_count()), proc_id, result)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()
    print(result)
    incorrect = sum(result)
    print('Combined result from all processes')
    print('total: {}, correct: {}, incorrect: {}, success rate: {}, time taken: {}'
          .format(total, total-incorrect, incorrect, (total-incorrect)/total*100, time.time()-t1))

