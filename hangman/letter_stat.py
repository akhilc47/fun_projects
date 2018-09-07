from pprint import pprint as pp
letter_matrix = [[0]*27 for _ in range(26)]
pp(letter_matrix)
with open('reduced_dict.txt', 'r') as fd:
    for word in fd:
        word = word[:-1]
        letter_matrix[ord(word[0])-97][0] += 1
        for i in range(len(word)-1):
            try:
                letter_matrix[ord(word[i+1])-97][ord(word[i])-96] += 1
            except IndexError:
                print(word, i)


with open('consecutive_letters.csv', 'w') as fout:
    fout.write('x,-,')
    for i in range(26):
        fout.write(chr(97+i)+',')
    fout.write('\n')
    for i in range(len(letter_matrix)):
        fout.write(chr(97+i)+',')
        for j in range(len(letter_matrix[0])):
            fout.write(str(letter_matrix[i][j])+',')
        fout.write('\n')
