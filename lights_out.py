input_array = []
for _ in range(3):
    row = list(map(int,input().split()))
    input_array.append(row)

light_array = [ 
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
]

for row in range(3):
    for col in range(3) :
        if input_array[row][col]%2 != 0 :

            light_array[row+1][col+1]= (light_array[row+1][col+1] + 1) % 2   #the light that was pressed

            light_array[row+1][col] = (light_array[row+1][col] + 1 ) % 2     #left

            light_array[row+1][col+2] = (light_array[row+1][col+2] + 1) % 2  #right

            light_array[row][col+1] = (light_array[row][col+1] + 1 ) % 2     #top

            light_array[row+2][col+1] = (light_array[row+2][col+1] + 1 ) % 2 #bottom
    
for row in range(1,4):
    for col in range(1,4):
        print(light_array[row][col],end='')
    print("")
