"""
import string
import random
key = 'AaBbCcDdEeFfGgHhJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'

a = 0
b = len(key)
for gen in range(len(key)):
    c = random.randint(0,length - 1)
    key = key + c
print(key[c])
print(b)

import random
key = 'AaBbCcDdEeFfGgHhJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
length = len(key)

for blah in range(len(key)): #Apologies for the lame variable names
    x = random.randint(0,length - 1)
    d = key[x]
    print(d)
"""

import random
seq = 'AaBbCcDdEeFfGgHhJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
a = "".join(random.sample(seq, len(seq)))
print(a)