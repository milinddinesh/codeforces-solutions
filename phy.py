n = int(input())

forces = []

for _ in range(n):
    forces.append(list(map(int,input().split())))

sum = 0

for i in range(3):
    for j in range(n):
        sum += forces[j][i]
    if sum != 0 :
        break

if sum!=0 :
    print("NO")
else : print("YES")
