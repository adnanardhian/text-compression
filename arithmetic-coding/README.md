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

