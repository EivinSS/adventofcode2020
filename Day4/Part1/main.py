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

for x in range(len(newline)-1):
    counter = 0
    for y in range(newline[x+1] - newline[x] - 1):
        for z in range(len(words)):
            if words[z] in content[newline[x]+1+y]:
                counter += 1
    if counter > 6:
        okpassport += 1

print(okpassport)

h.close()