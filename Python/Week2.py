#Problem 1

pi = [3,1,4,1,5,9]
e = [2,7,1]

h = 'harvey'
m = 'mudd'
c = 'college'

answer0 = [ e[0] ] + pi[-2:]  # [2,5,9]
answer1 = e[1:]
answer2 = pi[-1::-2]
answer3 = pi[1:]
answer4 = e[-1::-2] + pi[0::2]
answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
answer6 = c[0:4] + m[1:3] + c[-1]
answer7 = h[1:] + m[1:]
answer8 = h[0:3] + m[-1] + c[-1] + 3*h[0:3]
answer9 = c[3:6] + c[1] + m[0] + h[-1] + c[4:6] + c[1]
answer10 = c[0:5:2] + h[1:3] + c[0] + h[1] + c[2:4]

print (answer0)
print (answer1)
print (answer2)
print (answer3)
print (answer4)
print (answer5)
print (answer6)
print (answer7)
print (answer8)
print (answer9)
print (answer10)

#-----------------------------------------

#Problem 2


def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x

def sq(x):
    return x*x;

def interp(low, hi, fraction):
    return (hi-low)*fraction + low

def checkends(s):
    if s=='':
        return False
    elif s[0]==s[-1]:
        return True
    else:
        return False

def flipside(s):
    x = len(s)/2
    return s[x:] + s[0:x];

def convertFromSeconds(s):
    days    = (s/(60*60*24))
    s       = (s%(60*60*24))
    hours   = (s/(60*60))
    s       = (s%(60*60))
    minutes = (s/60)
    s       = (s%60)
    seconds = s
    return[days, hours, minutes, seconds]


def front3(str):
  return 3*str[0:3]
