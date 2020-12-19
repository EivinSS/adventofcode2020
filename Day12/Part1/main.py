h = open('Day12/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

for x in range(len(content)):
    if content[x].endswith('\n'):
        content[x] = content[x][:-1]

def turn(command, direction):
    degree = direction
    if command[0] == 'R':
        degreeR = (degree - int(command[1:])) % 360
        direction = degreeR
        
    if command[0] == 'L':
        degreeL = (degree + int(command[1:])) % 360
        direction = degreeL
    
    return direction

def move(command, direction):
    movingpos = []
    movingpos.append(0)
    movingpos.append(0)

    if command[0] == 'N':
        movingpos[1] = int(command[1:])
    elif command[0] == 'S':
        movingpos[1] = -int(command[1:])
    elif command[0] == 'E':
        movingpos[0] = int(command[1:])
    elif command[0] == 'W':
        movingpos[0] = -int(command[1:])
    else:
        if direction == 90:
            movingpos[1] = int(command[1:])
        elif direction == 270:
            movingpos[1] = -int(command[1:])
        elif direction == 0:
            movingpos[0] = int(command[1:])
        elif direction == 180:
            movingpos[0] = -int(command[1:])
    
    return movingpos

direction = 0
degree = 0

position = []
position.append(0)
position.append(0)

for x in range(len(content)):
    if str(content[x][0]) == 'R' or str(content[x][0]) == 'L' :
        direction = turn(content[x], direction)

    else:
        movingpos = move(content[x], direction)
        position[0] = position[0] + movingpos[0]
        position[1] = position[1] + movingpos[1]

print(position)
print(int(position[0]) + int(position[1]))


