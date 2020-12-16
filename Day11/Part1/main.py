h = open('Day11/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

for x in range(len(content)):
    if content[x].endswith('\n'):
        content[x] = content[x][:-1]

def occupiedAdjTo(x, y, which):
    adjOcc = 0

    if x == 0:
        if y == 0:
            if content[x][y+1] == which:
                adjOcc += 1
            if content[x+1][y] == which:
                adjOcc += 1
            if content[x+1][y+1] == which:
                adjOcc += 1
            return adjOcc

        if y == (len(content[x])-1):
            if content[x][y-1] == which:
                adjOcc += 1
            if content[x+1][y-1] == which:
                adjOcc += 1
            if content[x+1][y] == which:
                adjOcc += 1
            return adjOcc
        
        if content[x][y-1] == which:
            adjOcc += 1
        if content[x][y+1] == which:
            adjOcc += 1
        if content[x+1][y-1] == which:
            adjOcc += 1
        if content[x+1][y] == which:
            adjOcc += 1
        if content[x+1][y+1] == which:
            adjOcc += 1
        return adjOcc

    
    if x == (len(content)-1):
        if y == 0:
            if content[x-1][y] == which:
                adjOcc += 1
            if content[x-1][y+1] == which:
                adjOcc += 1
            if content[x][y+1] == which:
                adjOcc += 1
            return adjOcc

        if y == (len(content[x])-1):
            if content[x-1][y-1] == which:
                adjOcc += 1
            if content[x-1][y] == which:
                adjOcc += 1
            if content[x][y-1] == which:
                adjOcc += 1
            return adjOcc
        
        if content[x][y-1] == which:
            adjOcc += 1
        if content[x][y+1] == which:
            adjOcc += 1
        if content[x-1][y-1] == which:
            adjOcc += 1
        if content[x-1][y] == which:
            adjOcc += 1
        if content[x-1][y+1] == which:
            adjOcc += 1
        return adjOcc
    
    if y == 0:
        if content[x-1][y] == which:
            adjOcc += 1
        if content[x-1][y+1] == which:
            adjOcc += 1
        if content[x][y+1] == which:
            adjOcc += 1
        if content[x+1][y] == which:
            adjOcc += 1
        if content[x+1][y+1] == which:
            adjOcc += 1
        return adjOcc
    
    if y == (len(content[x])-1):
        if content[x-1][y] == which:
            adjOcc += 1
        if content[x-1][y-1] == which:
            adjOcc += 1
        if content[x][y-1] == which:
            adjOcc += 1
        if content[x+1][y] == which:
            adjOcc += 1
        if content[x+1][y-1] == which:
            adjOcc += 1
        return adjOcc
    
    #middle
    if content[x-1][y-1] == which:
        adjOcc += 1
    if content[x-1][y] == which:
        adjOcc += 1
    if content[x-1][y+1] == which:
        adjOcc += 1
    if content[x][y-1] == which:
        adjOcc += 1
    if content[x][y+1] == which:
        adjOcc += 1
    if content[x+1][y-1] == which:
        adjOcc += 1
    if content[x+1][y] == which:
        adjOcc += 1
    if content[x+1][y+1] == which:
        adjOcc += 1
    
    return adjOcc


for a in range(200):

    #print('content is  before ' + str(content))
    tempArray = content.copy()

    
    for x in range(len(content)):
        for y in range(len(content[x])):
            if content[x][y] == 'L':
                if occupiedAdjTo(x,y,'#') == 0:
                    list1 = list(tempArray[x])
                    list1[y] = '#'
                    tempArray[x] = "".join(list1)
            if content[x][y] == '#':
                if occupiedAdjTo(x,y,'#') >=4:
                    list2 = list(tempArray[x])
                    list2[y] = 'L'
                    tempArray[x] = "".join(list2)
    
    content = tempArray.copy()
    
    count = 0

    for x in range(len(content)):
        for y in range(len(content[x])):
            if content[x][y] == '#':
                count += 1

    print(count)


