from collections import Counter
freqlst = []
for i in range(0,97):
    handle = open("2.txt", "r")
    data = handle.read(1)
    freqlst.append(data)
    handle.close()
print(freqlst)