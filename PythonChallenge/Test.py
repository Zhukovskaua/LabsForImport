freqlst = []

handle = open("2.txt", "r")

while True:
    data = handle.read(1024)
    if not data:
        break

for i in range(0,99984):
    for j in data:
        print(j)
