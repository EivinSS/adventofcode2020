import re

h = open('Day4/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

words = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

newline = []
newline.append(-1)

okpassport = 0

for x in range(len(content)):
    if str(content[x]) == "\n":
        newline.append(x)

newline.append(1032)

for x in range(len(newline)-1):
    counter = 0
    for y in range(newline[x+1] - newline[x] - 1):
        print(content[newline[x]+1+y])
        if content[newline[x]+1+y].find('byr') != -1:
            index = content[newline[x]+1+y].find('byr')
            numb = int(content[newline[x]+1+y][index+4:index+8])
            if 1920 <= numb <2003:                
                    counter += 1

        if content[newline[x]+1+y].find('iyr') != -1:
            index = content[newline[x]+1+y].find('iyr')
            numb = int(content[newline[x]+1+y][index+4:index+8])
            if 2010 <= numb < 2021:                
                    counter += 1
        
        if content[newline[x]+1+y].find('eyr') != -1:
            index = content[newline[x]+1+y].find('eyr')
            numb = int(content[newline[x]+1+y][index+4:index+8])
            if 2020 <= numb <2031:                
                    counter += 1

        if content[newline[x]+1+y].find('hgt') != -1:
            index = content[newline[x]+1+y].find('hgt')
            if content[newline[x]+1+y].find('cm') != -1:
                cmindex = content[newline[x]+1+y].find('cm')
                cm = int(content[newline[x]+1+y][(index+4):cmindex])
                if 150 <= cm < 194:                
                    counter += 1

            if content[newline[x]+1+y].find('in') != -1:
                inindex = content[newline[x]+1+y].find('in')
                inc = int(content[newline[x]+1+y][(index+4):inindex])
                if 59 <= inc <77:                
                    counter += 1

        if content[newline[x]+1+y].find('hcl') != -1:
            index = content[newline[x]+1+y].find('hcl')
            stringTotal = content[newline[x]+1+y][index+4:]
            theCodeList = stringTotal.partition(' ')
            colorCode = theCodeList[0]
            match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', colorCode)
            if match:                
                counter += 1
                
        if content[newline[x]+1+y].find('ecl') != -1:
            index = content[newline[x]+1+y].find('ecl')
            color = content[newline[x]+1+y][index+4:index+7]
            if color == 'amb':
                counter += 1
            if color == 'blu':
                counter += 1
            if color == 'brn':
                counter += 1
            if color == 'gry':
                counter += 1
            if color == 'grn':
                counter += 1
            if color == 'hzl':
                counter += 1
            if color == 'oth':
                counter += 1
        
        if content[newline[x]+1+y].find('pid') != -1:
            index = content[newline[x]+1+y].find('pid')
            stringTotal = content[newline[x]+1+y][index+4:]
            theCodeList = stringTotal.partition(' ')
            pidCode = theCodeList[0].rstrip('\n')
            if len(pidCode) == 9 and int(pidCode) < 999999999+1 and int(pidCode) > 0:  
                counter += 1
               
    if counter > 6:
        okpassport += 1
    print(okpassport)
    
h.close()