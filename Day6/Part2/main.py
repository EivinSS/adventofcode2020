import string
import array

h = open('Day6/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

alphabet_string = string.ascii_lowercase

for x in range(len(content)-1):
    if len(content[x])>1:
        content[x] = content[x][:-1]

letter_list = []
sum = 0
start = True
for x in range(len(content)-1):

    if content[x+1] != '\n' and content[x] != '\n':
        if start:
            for y in range(len(content[x])):
                for z in range(len(content[x+1])):
                    if content[x][y] == content[x+1][z]:
                        letter_list.append(content[x][y])
        
        else:
            temp_list = []
            for y in range(len(letter_list)):
                for z in range(len(content[x+1])):
                    if letter_list[y] == content[x+1][z]:
                        temp_list.append(letter_list[y])
            letter_list.clear()
            letter_list = temp_list.copy()
            temp_list.clear()        

        start = False

    elif content[x] != '\n':
        sum += len(letter_list)
        start = True
        letter_list.clear()
    
    if content[x-1] == '\n' and content[x+1] == '\n':
        sum += len(content[x])
        

#getting the last segment
sum += len(letter_list)
print(str(sum) + 'sss')