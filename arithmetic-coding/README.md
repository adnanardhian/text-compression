Arithmetic coding of 26 lowercase letters separated by space (' '), stored in list of number that represent each word

compression
input : text, output : file containing list of number

decompression
input : file containing list of number, output : text


assuming each letter has the same probability which is 1/26 = 0.0384615385,

a = 0.0 - 0.0384615385

b = 0.0384615385 - 0.076923077

.

.

.

.

z = 0.9615384615 - 1.0


ouput of each word is a decimal number, A.BCDEF, where A is the length of word, and .BCDEF is the number itself

example,

text : ""the quick brown fox jumps over the lazy dog""

result = [3.741403993216093, 5.645430843780713, 5.06445524601157, 3.2143403741522483, 5.376456746373175, 4.5697921967285104, 3.7413790952071073, 4.4245534521059255, 3.136445274974985]

