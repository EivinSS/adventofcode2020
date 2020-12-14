h = open('Day10/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

# Adding first and last number in array
the_numbers = []
the_numbers.append(0)
the_numbers.append(189)

for x in range(len(content)):
    the_numbers.append(int(content[x]))

the_numbers.sort()

print(the_numbers)

# Recursive. This takes to long, but works with smaller examples
def run(x, paths):
    pathss = paths
    summing = 0
    for y in range(1,4):
        if x+y < execede:
            if the_numbers[x+y] - the_numbers[x] == 1:
                summing += run(x+y,pathss)
        if x+y < execede:
            if the_numbers[x+y] - the_numbers[x] == 2:
                summing += run(x+y,pathss)
        if x+y < execede:
            if the_numbers[x+y] - the_numbers[x] == 3:
                summing += run(x+y,pathss)
    
        if x+1 == execede:
            return 1
    pathss += summing
    summing = 0

    return pathss


# Array of how many options each number has
veier = []
for x in range(len(the_numbers)-1):

    summing = 0
    for y in range(1,4):
        if x+y < execede:
            if the_numbers[x+y] - the_numbers[x] == 1:
                summing += 1
        if x+y < execede:
            if the_numbers[x+y] - the_numbers[x] == 2:
                summing += 1
        if x+y < execede:
            if the_numbers[x+y] - the_numbers[x] == 3:
                summing += 1
    
    veier.append(summing)

# Array of how many times each number gets hit by another number
hitting = []
for y in range(len(veier)):
    hits = 0
    if y-1 >= 0:
        if veier[y-1] >=1:
            hits += 1
    if y-2 >= 0:
        if veier[y-2] >=2:
            hits += 1
    if y-3 >= 0:
        if veier[y-3] >=3:
            hits += 1
    hitting.append(hits)

#Adding last number 189
hitting.append(1)

# Array of how many occuranses there is of each number. The answer to the task is the last number
hvorMange = []

for x in range(len(the_numbers)):
    if hitting[x] == 0:
        hvorMange.append(1)
    if hitting[x] == 1:
        hvorMange.append(hvorMange[x-1])
    if hitting[x] == 2:
        hvorMange.append(hvorMange[x-1] + hvorMange[x-2])
    if hitting[x] == 3:
        hvorMange.append(hvorMange[x-1] + hvorMange[x-2] + hvorMange[x-3])

# Last number in array is answer
print(hvorMange)


