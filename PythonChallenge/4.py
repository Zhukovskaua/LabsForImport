from urllib.request import urlopen
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
number = str(16044/2)
pattern = re.compile("and the next nothing is (\d+)")

while True:
    rawpage = urlopen(url % number).read().decode('utf-8')
    print(rawpage)
    newnumber = pattern.search(rawpage)
    if newnumber == None:
        break
    number = newnumber.group(1)