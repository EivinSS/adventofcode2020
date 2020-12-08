h = open('Day7/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

contain = ['shiny gold']

def look():
    for y in range(len(content)):
        for z in range(len(contain)):
            if contain[z] in content[y]:
                res = content[y].split()
                bag = str(res[0]) + ' ' + str(res[1])
                if bag != contain[z] and bag not in contain:
                    contain.append(str(res[0]) + ' ' + str(res[1]))
    return (len(contain)-1)

last = 0
now = 1

while now > last:
    last = now
    now = look()
    print(now)
    if now == last:
        break



