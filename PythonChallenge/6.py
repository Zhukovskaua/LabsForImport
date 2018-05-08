import zipfile, re, string
file = zipfile.ZipFile("channel.zip")
num = '90052'
newnum = ''

def cleanraw(nextraw):
    print(nextraw)
    newnum = ''
    for i in nextraw:
        if i in string.digits:
            newnum += str(i)
    return(newnum)

nextraw = (file.read('%s.txt' % num).decode('utf-8'))
cleanraw(nextraw)
while True:
    nextraw = (file.read('%s.txt' % newnum).decode('utf-8'))
    cleanraw(nextraw)