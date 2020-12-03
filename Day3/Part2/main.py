import math

h = open('Day3/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

def calcTrees(right, down):
    trees = 0
    for x in range(math.floor((len(content)-1)/down)):
        if content[(down*x)+down][((right + (x * right)) % (len(content[x])-1))] == '#':
            trees += 1
    return trees

print(calcTrees(1,1)*calcTrees(3,1)*calcTrees(5,1)*calcTrees(7,1)*calcTrees(1,2))


