h = open('Day7/numbers.txt', 'r') 
  
# Reading from the file 
content = h.readlines()

def baggins(baggen, numb):
    for x in range(len(content)):
        if baggen in content[x]:
                res = content[x].split()
                firstpart = str(res[0]) + ' ' + str(res[1])
                if firstpart in baggen:
                    ind = res.index('contain')
                    if res[ind+1].isdigit():
                        summer = 0
                        for a in range(4, len(res)):
                            if res[a].isdigit():
                                word = str(res[a+1]) + ' ' + str(res[a+2])
                                howmany = int(res[a])
                                summer += baggins(word, howmany)
                        return numb * summer + numb         
                    else:
                        return (1 * numb)

print(baggins('shiny gold', 1)-1)

