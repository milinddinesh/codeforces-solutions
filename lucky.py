#lucky num = +ve int , decimals only contain 4 and 7 
#Eg : 123.47 , 21.7 , 31.4

num = input()

if '7' in num or '4' in num :
    count = num.count('7')+num.count('4')
    if count == 7 or count == 4:
        print("YES")
    else : print("NO")
else : print("NO")