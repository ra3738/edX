
# Problem 1

def isOdd(n):
    if (n%2 == 0):
        return False
    else:
        return True


def numToBinary(n):
    if (n==0):
        return ''
    elif (isOdd(n)):
        return numToBinary(n/2) + '1'
    else:
        return numToBinary(n/2) + '0'


# ---------------------
# Problem 2

def binaryToNum(n):
    if n=='':
        return 0

    elif n[0] == '1':
        return 2**(len(n)-1) + binaryToNum(n[1:])

    else:
        return binaryToNum(n[1:])

#def binaryToNum(S):
#  if S == '':
#    return 0
#
#  elif S[-1] == '1': 
#    return 2*binaryToNum(S[0:-1]) + 1
#
#  else:
#    return 2*binaryToNum(S[0:-1]) + 0


# ---------------------
# Problem 3

def increment(n):
    numVal = binaryToNum(n)
    numVal = numVal+1
    binVal = numToBinary(numVal)
    
    if (len(binVal) > 8):
        return binVal[-8:]

    else:
        return '0'*(8-len(binVal)) + binVal


# ---------------------
# Problem 3

def count(S, n):
    if n==0:
        print S
        return

    else:
        print S
        S = increment(S)
        return count(S, n-1)


# ---------------------
# Problem 4

def numToTernary(n):
    if (n==0):
        return ''
    elif (n%3 == 2):
        return numToTernary(n/3) + '2'
    elif (n%3 == 1):
        return numToTernary(n/3) + '1'
    else:
        return numToTernary(n/3) + '0'
    

def ternaryToNum(n):
    if n=='':
        return 0

    elif n[0] == '2':
        return 3**(len(n)-1)*2 + ternaryToNum(n[1:])

    elif n[0] == '1':
        return 3**(len(n)-1) + ternaryToNum(n[1:])

    else:
        return ternaryToNum(n[1:])


# ---------------------
# Problem 5

def balancedTernaryToNum(n):
    if n=='':
        return 0

    elif n[0] == '+':
        return 3**(len(n)-1) + balancedTernaryToNum(n[1:])

    elif n[0] == '-':
        return balancedTernaryToNum(n[1:]) - 3**(len(n)-1)

    else:
        return balancedTernaryToNum(n[1:])


def numToBalancedTernary(n):
    if (n==0):
        return ''
    elif (n%3 == 2):
        return numToBalancedTernary(n/3 + 1) + '-'
    elif (n%3 == 1):
        return numToBalancedTernary(n/3) + '+'
    else:
        return numToBalancedTernary(n/3) + '0'


# ---------------------
# Problem 6


def numToBaseB( N, B ):
    if (N == 0):
        return ''

    else:
        val = N%B
        return numToBaseB(N/B, B) + str(val)

def baseBToNum(S, B):
    if (S == ''):
        return 0

    else:
        return ( (B**(len(S)-1)) * int(S[0]) ) + baseBToNum(S[1:], B)


# ---------------------
# Problem 7

def baseToBase(B1,B2,s_in_B1):
    val1 = baseBToNum(s_in_B1, B1)
    val2 = numToBaseB(val1, B2)
    return val2


# ---------------------
# Problem 8

def add(S,T):
    












