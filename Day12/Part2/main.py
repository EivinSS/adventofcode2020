import math

h = open('Day12/numbers.txt', 'r') 

  
# Reading from the file 
content = h.readlines()

for x in range(len(content)):
    if content[x].endswith('\n'):
        content[x] = content[x][:-1]

def turn(command, position, waypoint):
    xvec = waypoint[0] - position[0]
    yvec = waypoint[1] - position[1]
    if command[0] == 'R':
        if int(command[1:]) == 90:
            waypoint[0] = position[0] + yvec
            waypoint[1] = position[1] - xvec
        if int(command[1:]) == 180:
            waypoint[0] = position[0] - xvec
            waypoint[1] = position[1] - yvec
        if int(command[1:]) == 270:
            waypoint[0] = position[0] - yvec
            waypoint[1] = position[1] + xvec

    if command[0] == 'L':
        if int(command[1:]) == 90:
            waypoint[0] = position[0] - yvec
            waypoint[1] = position[1] + xvec
        if int(command[1:]) == 180:
            waypoint[0] = position[0] - xvec
            waypoint[1] = position[1] - yvec
        if int(command[1:]) == 270:
            waypoint[0] = position[0] + yvec
            waypoint[1] = position[1] - xvec

def moveWaypoint(command):
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

    return movingpos

def movePosition(command, position, waypoint):
   
    xvec = waypoint[0] - position[0]
    yvec = waypoint[1] - position[1]

    distance = int(command[1:])

    position[0] = position[0] + xvec*distance
    position[1] = position[1] + yvec*distance

    waypoint[0] = position[0] + xvec
    waypoint[1] = position[1] + yvec

position = []
position.append(0)
position.append(0)

waypoint = []
waypoint.append(10)
waypoint.append(1)

for x in range(len(content)):
    if str(content[x][0]) == 'R' or str(content[x][0]) == 'L':
        turn(content[x], position, waypoint)

    elif str(content[x][0]) == 'F':
        movePosition(content[x], position, waypoint)
    
    else:
        movingpos = moveWaypoint(content[x])
        waypoint[0] = waypoint[0] + movingpos[0]
        waypoint[1] = waypoint[1] + movingpos[1]

    #print('x: ' + str(x+1) +  ', ' + 'pos: ' + str(position) + ', way: ' + str(waypoint))
    #print()

print(abs(int(position[0])) + abs(int(position[1])))