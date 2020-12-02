h = open('Day2/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

valid = 0

for x in range(len(content)):
    print(content[x])
    strek = content[x].find('-')
    kol = content[x].find(':')
    if strek == 1 and kol == 5:
        first = int(content[x][0])
        second = int(content[x][2])
    elif strek == 1 and kol == 6:
        first = int(content[x][0])
        second = int((content[x][2]+content[x][3]))
    elif strek == 2 and kol == 6:
        first = int((content[x][0]+content[x][1]))
        second = int(content[x][3])
    elif strek == 2 and kol == 7:
        first = int((content[x][0]+content[x][1]))
        second = int((content[x][3]+content[x][4]))
    
    letter = content[x][kol-1]
    password = content[x][(kol+2):len(content[x])]

    count = 0
    if password[first-1] == letter:
        count += 1
    if password[second-1] == letter:
        count += 1

    if count == 1:
        valid += 1
    # print('first: ' + password[first-1])
    # print('second: ' + password[second-1])
    # print('letter: ' + letter)

print('valid: ' + str(valid))

            