#!/usr/bin/env python3

import math 
a , b    = map(int , input().split())

def is_prime(num):
    if num > 2 and  num%2 == 0 :
        return False

    elif num%3 == 0 :
        return False 

    else :
        for i in range( 5 , int(math.sqrt(num))+1, 2 ) :
            if num%i == 0 :
                return False
        return True

i = a + 1
first = False

if is_prime(b):
    while i<=b :
        if is_prime(i):
            if i == b :
                first = True
                break
            else : 
                break
        i += 1

if first : 
    print("YES")
else : print("NO")








