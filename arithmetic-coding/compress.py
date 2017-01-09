import random
import pickle

DICT = 'abcdefghijklmnopqrstuvwxyz'
SENTENCE = "the quick brown fox jumps over the lazy dog"
FIN_RES = []

#Compressing Each Words
def getVal(words):
    init_range = 1
    start = 0
    for i in range(0,len(words)):
        init_range = init_range/26.0
        min_val = DICT.index(words[i])*init_range
        start += min_val
        max_val = start + init_range
    return len(words) + random.uniform(start,max_val)

if __name__ == '__main__':
    list_of_sent = SENTENCE.split(' ')
    for i in range(0,len(list_of_sent)):
        FIN_RES.append(getVal(list_of_sent[i]))
    
    with open('compressedfile', 'wb') as fp:
        pickle.dump(FIN_RES, fp)
