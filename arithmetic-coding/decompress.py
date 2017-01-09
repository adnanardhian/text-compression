import pickle

DICT = 'abcdefghijklmnopqrstuvwxyz'
FIN_RES = ''

#Helper Function to Decompress
def getIdx(n,maxs,jump):
    idx = 0    
    while True:
        if n < maxs:
            return [idx,maxs]
        else:
            maxs+=jump
            idx+=1

#Decompressing each number, get the words back
def getWords(val):
    word_len = int(val)
    word_val = val - word_len
    mins = 0.0
    res = ''
    for i in range(0,word_len):
        jump = 1.0/(26**(i+1))
        indexs = getIdx(word_val,mins+jump,jump)[0] 
        mins = getIdx(word_val,mins+jump,jump)[1] - jump
        res+=DICT[indexs]
    return res

if __name__ == '__main__':
    with open ('compressedfile', 'rb') as fp:
        itemlist = pickle.load(fp)
    for item in itemlist:
        FIN_RES+=getWords(item)
        FIN_RES+=' '
    FIN_RES = FIN_RES[:-1]
    
    print FIN_RES
