h = open('Day9/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

number = 22406676

found = False

for x in range(len(content)):
    if found:
        break
    sum = 0

    for y in range(len(content)):
        
        sum += int(content[x+y])
        
        if sum > number:
            print('To high')
            break
        
        if sum == number:
            print('Found! first: ' + str(content[x]) + ', last: ' + str(content[x+y]) + ', in the set')
            found = True
            index_first = content.index((content[x]))
            index_last = content.index((content[x+y]))
            my_set = []
            
            for z in range(index_first, index_last):
                my_set.append(int(content[z]))
            
            print('lowest value = ' + str(min(my_set)) + ', highest value = ' + str(max(my_set)) + ', sum = ' + str(int(min(my_set)) + int(max(my_set))))
            
            break
            

