word = list(input())
upper = lower = 0
for char in word :
    if char.isupper() :
        upper+= 1
    else : lower += 1

if upper > lower :
    print(''.join(word).upper())
else : print(''.join(word).lower())