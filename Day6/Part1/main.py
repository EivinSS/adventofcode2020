import string

h = open('Day6/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

alphabet_string = string.ascii_lowercase

for x in range(len(content)-1):
    if len(content[x])>1:
        content[x] = content[x][:-1]

letter_list = []
sum = 0
for x in range(len(content)):

    if content[x] != '\n':
        for y in range(len(content[x])):
            
            if content[x][y] not in letter_list:
                letter_list.append(content[x][y])

    else:
        sum += len(letter_list)
        letter_list.clear()

#getting the last segment
sum += len(letter_list)
letter_list.clear()

print(sum)