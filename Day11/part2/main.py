h = open('Day11/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

for x in range(len(content)):
    if content[x].endswith('\n'):
        content[x] = content[x][:-1]

def occupiedDiagonaly(x, y, which):
    adjOcc = 0

    # Up
    if x > 0:
        for a in range(x-1, -1, -1):
            if content[a][y] == 'L':
                break
            if content[a][y] == which:
                adjOcc += 1
                #print('Up')
                break
    
    # Down
    if x < len(content)-1:
        for a in range(x+1, len(content)):
            if content[a][y] == 'L':
                break
            if content[a][y] == which:
                adjOcc += 1
                #print('Down')
                break
    
    # Right
    if y < len(content[x])-1:
        for a in range(y+1, len(content[x])):
            if content[x][a] == 'L':
                break
            if content[x][a] == which:
                adjOcc += 1
                #print('Right')
                break
    
    # Left
    if y > 0:
        for a in range(y-1, -1, -1):
            if content[x][a] == 'L':
                break
            if content[x][a] == which:
                adjOcc += 1
                #print('Left')
                break
    
    # Top-Right
    if x > 0 and y < len(content[x])-1:        
        a = -1
        b = 1
        edge = False
        while not edge:
            if content[x+a][y+b] == 'L':
                break
            if content[x+a][y+b] == which:
                adjOcc += 1
                #print('Top-Right')
                break
            
            if x + a == 0 or y + b == len(content[x])-1:
                edge = True

            a -= 1
            b += 1

    # Top-Left
    if x > 0 and y > 0:        
        a = -1
        b = -1
        edge = False
        while not edge:
            if content[x+a][y+b] == 'L':
                break
            if content[x+a][y+b] == which:
                adjOcc += 1
                #print('Top-Left')
                break
            
            if x + a == 0 or y + b == 0:
                edge = True

            a -= 1
            b -= 1
    
    # down-Left
    if x < len(content)-1 and y > 0:        
        a = 1
        b = -1
        edge = False
        while not edge:
            if content[x+a][y+b] == 'L':
                break
            if content[x+a][y+b] == which:
                adjOcc += 1
                #print('Down-Left')
                break

            if x + a == len(content)-1 or y + b == 0:
                edge = True
            
            a += 1
            b -= 1
    
    # down-right
    if x < len(content)-1 and y < len(content[x])-1:        
        a = 1
        b = 1
        edge = False
        while not edge:
            if content[x+a][y+b] == 'L':
                break
            if content[x+a][y+b] == which:
                adjOcc += 1
                #print('Down-Right')
                break
            
            if x + a == len(content)-1 or y + b == len(content[x])-1:
                edge = True

            a += 1
            b += 1

    #print(adjOcc)
    return adjOcc


#for a in range(100):

a = 1
b = 2
count = 0

while a != b:

    #print('content is  before ' + str(content))
    tempArray = content.copy()

    
    for x in range(len(content)):
        for y in range(len(content[x])):
            #print('x: ' +str(x) + 'y: '+str(y))
            if content[x][y] == 'L':
                if occupiedDiagonaly(x,y,'#') == 0:
                    list1 = list(tempArray[x])
                    list1[y] = '#'
                    tempArray[x] = "".join(list1)
            if content[x][y] == '#':
                #print(occupiedDiagonaly(x,y,'#'))
                if occupiedDiagonaly(x,y,'#') >=5:
                    list2 = list(tempArray[x])
                    list2[y] = 'L'
                    tempArray[x] = "".join(list2)
    
    content = tempArray.copy()
    #print(content)
    count = 0

    for x in range(len(content)):
        for y in range(len(content[x])):
            if content[x][y] == '#':
                count += 1

    b = a
    a = count

print(count)