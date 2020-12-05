h = open('Day5/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

maxID = 0

lists = [[0]*8 for _ in range(128)]

for i in range(len(content)):
    lower = 0
    upper = 127
    for j in range(7):
        possibleSeats = upper - lower + 1
        if content[i][j] == 'F':
            upper = upper - (possibleSeats/2)
        if content[i][j] == 'B':
            lower = lower + (possibleSeats/2)
    
    left = 0
    right = 7
    for j in range(7, 10):
        possibleSeats = right - left + 1
        if content[i][j] == 'L':
            right = right - (possibleSeats/2)
        if content[i][j] == 'R':
            left = left + (possibleSeats/2)

    lists[int(upper)][int(right)] = 1

for i in range(40,80):
    for j in range(0,8):
        if lists[int(i)][int(j)] == 0:
            id = i*8+j
            print(f'ID: {id}')