h = open('Day2/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

valid = 0

for x in range(len(content)):
    print(content[x])
    strek = content[x].find('-')
    kol = content[x].find(':')
    if strek == 1 and kol == 5:
        lowest = int(content[x][0])
        highest = int(content[x][2])
    elif strek == 1 and kol == 6:
        lowest = int(content[x][0])
        highest = int((content[x][2]+content[x][3]))
    elif strek == 2 and kol == 6:
        lowest = int((content[x][0]+content[x][1]))
        highest = int(content[x][3])
    elif strek == 2 and kol == 7:
        lowest = int((content[x][0]+content[x][1]))
        highest = int((content[x][3]+content[x][4]))
    
    letter = content[x][kol-1]
    password = content[x][(kol+2):len(content[x])]

    count = 0
    for i in password: 
        if i == letter:
            count += 1
    
    if lowest <= count <= highest:
        valid += 1
    # print(lowest)
    # print(highest)
    # print(letter)
    # print('count: ' + str(count))
print('valid: ' + str(valid))

            