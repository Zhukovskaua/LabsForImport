import pickle
from urllib.request import urlopen
source = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
raw = pickle.load(source)
for line in raw:
    print("".join([a * b for b, a in line]))