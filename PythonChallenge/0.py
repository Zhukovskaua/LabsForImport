from urllib.request import Request, urlopen
from urllib.error import HTTPError
import string

bad = 0
good = 0
char0 = ''
char1 = ''


def search_bad_urls(srchin):
    req = Request(srchin)
    try:
        response = urlopen(srchin)
    except HTTPError as e:
        if e.code == 404:
            print(srchin,'Bad')
            return False
    else:
        print(srchin, 'Good')
        return True


if search_bad_urls(srchin='http://www.pythonchallenge.com/pc/def/2**38.html') == True:
    print("Test OK\nStarting Parse")
else:
    exit('Parcing Failed!')

print('Parsing digits')
for c0 in string.digits:
    break
    char0 = c0
    for c1 in string.digits:
        char1 = c1
        srchin = ('http://www.pythonchallenge.com/pc/def/2%c%c38.html' % (char0, char1))
        if search_bad_urls(srchin) == False:
            bad += 1
            print('Good:', good, ',Bad:', bad)
        else:
            good += 1
            print('Good:', good, ',Bad:', bad)
            break

print('Parsing letters')
for c0 in string.ascii_letters:
    break
    char0 = c0
    for c1 in string.ascii_letters:
        char1 = c1
        srchin = ('http://www.pythonchallenge.com/pc/def/2%c%c38.html' % (char0, char1))
        if search_bad_urls(srchin) == False:
            bad += 1
            print('Good:', good, ',Bad:', bad)
        else:
            good += 1
            print('Good:', good, ',Bad:', bad)
            break

print('Stop making everything too complicated')
flag = 2 ** 38
srchin = ('http://www.pythonchallenge.com/pc/def/%d.html' % flag)
if search_bad_urls(srchin) == False:
    bad += 1
    print('Good:', good, ',Bad:', bad)
else:
    good += 1
    print('Good:', good, ',Bad:', bad)
    exit('Answer found!')