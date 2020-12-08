h = open('Day8/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

nops = []
for a in range(len(content)):
    if 'nop' in content[a]:
        nops.append(a)

jmps = []
for b in range(len(content)):
    if 'jmp' in content[b]:
        jmps.append(b)

accumulator = 0

index = 0
found = False

visitedindexes = []

i=0

for c in range(len(jmps)):
    if found:
        break
    sed = content[jmps[c]]
    content[jmps[c]] = 'nop' + str(content[jmps[c]][3:])
    print('changing from ' + str(sed) + ' to ' + str(content[jmps[c]]) + ' on c-number = ' + str(c))

    while i < 2000:

        if 'FIN' in content[index]:
            print('i = ' + str(i) + ', We have terminated! I hope. Accumulator: ' + str(accumulator) + ' on c-number = ' + str(c) + ' of total ' + str(len(jmps)))
            found = True
            break

        if 'acc' in content[index]:
            last = index
        
            if index in visitedindexes:
                print('WARNING, ACC, index: ' + str(index) + ', accumulator: ' + str(accumulator) + ', c-number = ' + str(c))
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
                print('WARNING, NOP, index: ' + str(index) + ', accumulator: ' + str(accumulator) + ', c-number = ' + str(c))
                break

            visitedindexes.append(index)
            print('NOP, index: ' + str(index) + ', accumulator: ' + str(accumulator))
            index += 1
        

        if 'jmp' in content[index]:
            last = index

            if index in visitedindexes:
                print('WARNING, JMP, index: ' + str(index) + ', accumulator: ' + str(accumulator) + ', c-number = ' + str(c))
                break

            visitedindexes.append(index)

            num = content[index].split()
            if num[1][0] == '+':
                index += int(num[1][1:])
            if num[1][0] == '-':
                index -= int(num[1][1:])
        
            print('JMP, index: ' + str(last) + ', accumulator: ' + str(accumulator) + '. Jumping to index: ' + str(index))
        i += 1

    print('out of while, found = ' + str(found))
    i = 0
    accumulator = 0
    index = 0
    visitedindexes.clear()
    content[jmps[c]] = 'jmp' + str(content[jmps[c]][3:])
    print('changing back to ' + str(content[jmps[c]]))

print('we are done')

    

