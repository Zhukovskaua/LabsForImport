handle = open("2.txt", "r")
text = handle.read()
print(''.join(e for e in text if e.isalnum()))