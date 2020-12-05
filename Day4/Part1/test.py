substringlist = ["tack", "ac", "ckk"]
stri = "stack"

count = 0
for x in range(len(substringlist)):
    if substringlist[x] in stri:
        count += 1

print(count)
