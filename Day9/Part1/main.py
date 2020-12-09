h = open('Day9/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

for x in range(25, len(content)):
    
    found = False
    for y in range(1, 26):
        if found:
            break
        for z in range(1, 26):
            sum = 0
            if int(content[x-y]) != int(content[x-z]):
                sum = int(content[x-y]) + int(content[x-z])
                #print('X = ' + str(x) + ', adding y = ' + str(content[x-y]) + 'and z = ' + str(content[x-z]) + ', to be = ' + str(sum) + '. Is it the value == ' + str(content[x]))
                if sum == int(content[x]):
                    found = True
                    break
    if found:
        print('There is a sum, move on')
    if not found:
        print('No sum of number: ' + str(content[x]) + ', on index: ' + str(x))
        break