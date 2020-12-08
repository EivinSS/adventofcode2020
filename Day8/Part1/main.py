h = open('Day8/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

accumulator = 0

index = 0

visitedindexes = []

sometrue = True
i=0
while sometrue:
#while i < 40:
    if 'acc' in content[index]:
        last = index
        
        if index in visitedindexes:
            print('WARNING, ACC, index: ' + str(index) + ', accumulator: ' + str(accumulator))
            break

        visitedindexes.append(index)

        num = content[index].split()
        if num[1][0] == '+':
            accumulator += int(num[1][1:])
        if num[1][0] == '-':
            accumulator -= int(num[1][1:])
        index += 1
        print('ACC, index: ' + str(last) + ', accumulator: ' + str(accumulator))
        

    if 'nop' in content[index]:
        if index in visitedindexes:
            print('WARNING, NOP, index: ' + str(index) + ', accumulator: ' + str(accumulator))
            break

        visitedindexes.append(index)
        print('NOP, index: ' + str(index) + ', accumulator: ' + str(accumulator))
        index += 1
        

    if 'jmp' in content[index]:
        last = index

        if index in visitedindexes:
            print('WARNING, JMP, index: ' + str(index) + ', accumulator: ' + str(accumulator))
            break

        visitedindexes.append(index)

        num = content[index].split()
        if num[1][0] == '+':
            index += int(num[1][1:])
        if num[1][0] == '-':
            index -= int(num[1][1:])
        
        print('JMP, index: ' + str(last) + ', accumulator: ' + str(accumulator) + '. Jumping to index: ' + str(index))
    
    #i += 1
print('stop pls')

    

