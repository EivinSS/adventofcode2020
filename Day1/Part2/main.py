h = open('Day1/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines() 

foundSum = False

# Iterating through the content of the file 
for x in range(0, len(content)): 
    for y in range(x+1, len(content)):
        for z in range(y+1, len(content)):
            sum2020 = int(content[x]) + int(content[y]) + int(content[z])
            if sum2020 == 2020:
                foundSum = True
                print('First number: %d, second number: %d, third number: %d' % (int(content[x]), int(content[y]), int(content[z])))
                break
        if(foundSum):
            break
    if(foundSum):
        break

h.close() 