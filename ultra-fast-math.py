#! /usr/bin/env python3

num1 = list(input())
num2 = list(input())

result = ''

for i in range(len(num1)):
    result += str(int(num1[i])^int(num2[i]))

print(result)



