h = open('Day10/tes.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

the_numbers = []
the_numbers.append(0)
the_numbers.append(22)
jolt_1 = 0
jolt_3 = 0
jolt_2 = 0

for x in range(len(content)):
    the_numbers.append(int(content[x]))

the_numbers.sort()
print(the_numbers)

for y in range(len(the_numbers)-1):
    if (the_numbers[y+1] - the_numbers[y]) == 1:
        jolt_1 += 1
    if (the_numbers[y+1] - the_numbers[y]) == 3:
        jolt_3 += 1
    if (the_numbers[y+1] - the_numbers[y]) == 2:
        jolt_2 += 1

print(jolt_1)
print(jolt_3)
print(jolt_2)
print(int(jolt_1*jolt_3))


choises = 0




    

