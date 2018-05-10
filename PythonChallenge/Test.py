cryp = input()
cryp = cryp.lower()
d = {}
for i in cryp:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)