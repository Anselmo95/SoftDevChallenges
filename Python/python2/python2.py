#!/usr/bin/python
import socket
import pickle
import datetime

num = {
    -12976824096487209450: 0,
    54347709561699389752: 1,
    18538036056993905567: 2,
    28599134791804223254: 3,
    16491610649247999124: 4,
    18538036056993905573: 5,
    15294407690905719788: 6,
    -14007435434038523485: 7,
    22111878059627851692: 8,
    25355506425716037472: 9
}


month = {   
    'Jan':1,
    'Feb':2,
    'Mar':3,
    'Apr':4,
    'May':5,
    'Jun':6,
    'Jul':7,
    'Aug':8,
    'Sep':9,
    'Oct':10,
    'Nov':11,
    'Dec':12    
}

name = 'Ansel'
my_secret = '2a7b69c96bf4bc6d3832d09f9ab21ded'


def readNlines( fs, n = 1, strip = 0 ):
    lines = []
    for i in range(n):
        line = fs.readline().rstrip('\n')
        #print i, line
        lines.append(line)
    if n == 1:
        return line
    else:
        return lines



def guessAnumber(fs):
    upper = (1 << 20)
    lower = 0
    for i in range(20):
        guess = ((upper+lower) >> 1)
        #print guess
        fs.write(str(guess) + '\n')
        line = readNlines(fs).split()
        if line[0] == 'BRAVO':
            return
        elif line[3] == 'smaller':
            upper = guess
        else:
            lower = guess
        

def recogNumber(fs):
    res1 = 0
    res2 = 0
    res3 = 0
    for idx,x in enumerate(readNlines(fs,7)):
        if idx == 1:
            res1-= hash(x[:7])  
            res2-= hash(x[16:23])
            res3-= hash(x[32:].ljust(7))
        else:
            res1+= hash(x[:7])  
            res2+= hash(x[16:23])
            res3+= hash(x[32:].ljust(7))

    return str(num[res1]) + str(num[res2]) + str(num[res3])

def getMicro(fs):
    pick_time = '\n'.join(readNlines(fs,8))
    depick_time = pickle.loads(pick_time)
    return str(depick_time.microsecond)

def getDeltaTime(fs):
    a = readNlines(fs,2)
    a = a[1].split()
    today = datetime.datetime.now()
    date = datetime.datetime(2000+int(a[7].strip('.')),month[a[6]],int(a[5]))
    delta = today - date
    return str(delta.days)

def getSecret(fs):
    a = readNlines(fs,3)
    return a[2]

address = ('localhost',9999)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect(address)

fs = soc.makefile('rw',0)

readNlines(fs,2)
fs.write(name + '\n')
readNlines(fs)
fs.write(my_secret + '\n')
readNlines(fs)
guessAnumber(fs)
sol = recogNumber(fs)
readNlines(fs,2)
fs.write(sol + '\n')
readNlines(fs,2)
micro = getMicro(fs)
readNlines(fs,2)
fs.write(micro + '\n')
days = getDeltaTime(fs)
fs.write(days + '\n')
secret = getSecret(fs)
print secret
