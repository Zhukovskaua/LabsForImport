import zipfile
import string
file = zipfile.ZipFile("channel.zip")
num = '90052'
collect = 0
comments = []
def cleanraw(nextraw):
    print(nextraw)
    newnum = ''
    for i in nextraw:
        if i in string.digits:
            newnum += str(i)
    if newnum == '':
        return 0
    return(newnum)



nextraw = (file.read('%s.txt' % num).decode('utf-8'))
comments.append(str((file.getinfo('%s.txt' % num).comment.decode("utf-8"))))
print('nextraw', nextraw)
newnum = cleanraw(nextraw)
while True:
    if newnum == 0:
        print(collect)
        print("".join(comments))
        break
    collect += int(newnum)
    nextraw = (file.read('%s.txt' % newnum).decode('utf-8'))
    comments.append(str((file.getinfo('%s.txt' % newnum).comment.decode("utf-8"))))
    newnum = cleanraw(nextraw)
