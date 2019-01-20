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
"""
import random
keyres = 'AaBbCcDdEeFfGgHhJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
keys = 3
for keys in range(keys):
    a = "".join(random.sample(keyres, len(keyres)))
print(a)
"""

import random
keyres = 'AaBbCcDdEeFfGgHhJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
keys = 3
for _ in range(keys):
    a = (''.join(random.choice(keyres) for _ in range(len(keyres))))
    print(a)