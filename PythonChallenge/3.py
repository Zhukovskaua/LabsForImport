import string
import re
handle = open("3.txt", "r")
text = handle.read()
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", text)))



