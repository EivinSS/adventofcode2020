h = open('Day3/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

trees = 0

for x in range(len(content)-1):
    if content[x+1][((3 + (x * 3)) % (len(content[x])-1))] == '#':
        trees += 1

print(trees)