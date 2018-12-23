
# Problem 1

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.


def mutate(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = 1 + oldL[i]
    return new_ith_element

def mutate0(i, oldL):
    return 2*oldL[i]

def mutate1(i, oldL):
    return oldL[i] * oldL[i]

def mutate2(i, oldL):
    return oldL[(i-1)]  

def mutate3(i, oldL):
    return choice([0,1])

def mutate4(i, oldL, user=0):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    if i == user:
        new_ith_element = 1        # this makes the game easy!
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element

def mutate5(i, oldL, user=0):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    if i == user:
        if oldL[i] == 1:
            new_ith_element = 0        # this makes the game easy!
        else:
            new_ith_element = 1  
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element

def mutate6(i, oldL, user=0):
    """ takes as input an index (i) and an old list (oldL)
        mutate returns the ith element of a NEW list!
        * note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve
    """
    if i == user or i == user-1 or i == user+1:
        if oldL[i] == 1:
            new_ith_element = 0        # this makes the game easy!
        else:
            new_ith_element = 1  
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element



def randBL(n):
    if n == 0:
        return []
    else:
        return [choice([0,1])] + randBL(n-1)


def allOnes(tempList):
    if len(tempList) == 0:
        return True
    elif tempList[0] != 1:
        return False
    else:
        return allOnes(tempList[1:])
    

def evolve(oldL, curgen = 0):
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    print oldL,                    # print the old list, L
    print "  (gen: " + str(curgen) + ")",  # and its gen.
    time.sleep(0.15)
    
    if allOnes(oldL):  # we're done!
        return curgen       # no return value... yet
    else:
        user = choice(range(len(oldL)))
        print "   index:" + str(user)
        newL = [ mutate6(i,oldL,user) for i in range(len(oldL)) ]
        return evolve(newL, curgen + 1)


# -----------------------------------
# Problem 2

def rot(c,n):
    if ('a' <= c <= 'z'):
        temp = (ord(c) + n)%123
        if temp < 26:
            return chr(97+temp)
        else:
            return chr(temp)

    elif ('A' <= c <= 'Z'):
        temp = (ord(c) + n)%91
        if temp < 26:
            return chr(65+temp)
        else:
            return chr(temp)
    else:
        return c


def encipher(code, key):
    if len(code) == 0:
        return ""
    else:
        return rot(code[0], key) + encipher(code[1:], key)

def decipher(code):
    newCodeList = [encipher(code, i) for i in range(26)]
    scoresList = [computeScore(i) for i in newCodeList]
    maxValIndex = maxScore(scoresList, len(scoresList)-1, 0)
    return newCodeList[maxValIndex]
    

def maxScore(code, counter, maxIndex):
    if counter == 0:
        return maxIndex
    else:
        if (code[counter]>=code[maxIndex]):
            return maxScore(code, counter-1, counter)
        else:
            return maxScore(code, counter-1, maxIndex)
    

def computeScore(code):
    if len(code) == 0:
        return 0
    else:
        return letProb(code[0]) + computeScore(code[1:])

def letProb( c ):
  """ if c is the space character or an alphabetic character,
    we return its monogram probability (for english),
    otherwise we return 1.0 We ignore capitalization.
    Adapted from
    http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
  """
  if c == ' ': return 0.1904
  if c == 'e' or c == 'E': return 0.1017
  if c == 't' or c == 'T': return 0.0737
  if c == 'a' or c == 'A': return 0.0661
  if c == 'o' or c == 'O': return 0.0610
  if c == 'i' or c == 'I': return 0.0562
  if c == 'n' or c == 'N': return 0.0557
  if c == 'h' or c == 'H': return 0.0542
  if c == 's' or c == 'S': return 0.0508
  if c == 'r' or c == 'R': return 0.0458
  if c == 'd' or c == 'D': return 0.0369
  if c == 'l' or c == 'L': return 0.0325
  if c == 'u' or c == 'U': return 0.0228
  if c == 'm' or c == 'M': return 0.0205
  if c == 'c' or c == 'C': return 0.0192
  if c == 'w' or c == 'W': return 0.0190
  if c == 'f' or c == 'F': return 0.0175
  if c == 'y' or c == 'Y': return 0.0165
  if c == 'g' or c == 'G': return 0.0161
  if c == 'p' or c == 'P': return 0.0131
  if c == 'b' or c == 'B': return 0.0115
  if c == 'v' or c == 'V': return 0.0088
  if c == 'k' or c == 'K': return 0.0066
  if c == 'x' or c == 'X': return 0.0014
  if c == 'j' or c == 'J': return 0.0008
  if c == 'q' or c == 'Q': return 0.0008
  if c == 'z' or c == 'Z': return 0.0005
  return 1.0


# -----------------------------------
# Problem 3

def blsort(binaryList):
    totalOnes = countOnes(binaryList);
    return [0]*(len(binaryList)-totalOnes) + ([1]*totalOnes)

def countOnes(binaryList):
    if binaryList == []:
        return 0
    else:
        if (binaryList[0] == 1):
            return 1 + countOnes(binaryList[1:])
        else:
            return countOnes(binaryList[1:])
    

# -----------------------------------
# Problem 4

def gensort(L):
    if L == []:
        return[]
    else:
        maxVal = max(L);
        L.remove(maxVal);
        return gensort(L) + [maxVal]


# -----------------------------------
# Problem 5

def jscore(S,T, counter = 0):
    if len(S)==0 or len(T)==0:
        return 0

    else:
        if S[0] in T:
            numInS = count(S[0], S)
            numInT = count(S[0], T)
            lowerVal = min(numInS, numInT)
            for letter in S[0]:
                S = S.replace(letter, '')
            return lowerVal + jscore(S,T, counter+1)

        else:
            return jscore(S[1:], T, counter+1)


def count(e,L):
    if (len(L) == 0):
        return 0
    
    if (e == L[0]):
        return 1 + count(e, L[1:])

    else:
        return count(e, L[1:])


# -----------------------------------
# Problem 6

def exact_change(target_amount, L):
    if target_amount==0 and L==[]:
        return True
    
    elif target_amount == 0:
        return True

    elif target_amount<0:
        return False

    elif target_amount!=0 and L==[]:
        return False

    else:
        useIt = exact_change(target_amount - L[0], L[1:])
        loseIt = exact_change(target_amount, L[1:])
        return useIt or loseIt


# -----------------------------------
# Problem 7

def LCS(S,T):
    if (S=='' or T==''):
        return ''

    elif (S[0]==T[0]): 
        return S[0] + LCS(S[1:], T[1:])

    else:
        result1 = LCS(S[1:], T)
        result2 = LCS(S, T[1:])
        return max([result1, result2], key=len)


















# -----------------------------------



def maxRevenue(L):
    maxList = [maxRelative(L, i) for i in range(len(L))]
    maxValue = max(maxList)
    return maxValue

def maxRelative(L, i, counter = 0):
    if counter == len(L):
        return 0

    else:
        if (L[counter]>=L[i]):
            return L[i] + maxRelative(L, i, counter+1)
        else:
            return maxRelative(L, i, counter+1)


    
##def doubleWithRecursion(L):
##
##    if len(L) == 0:
##        return L
##
##    else:
##        return [L[0] * 2] + doubleWithRecursion(L[1:])
##
##
##def dbl(N):
##    return N*2
##
##def doubleWithListComp(L):
##    return [(i*2) for i in L]
##
##def squareEach(L):
##    return [x*x for x in L]
##
##def complexListComp():
##    L = range(-6,7)
##
##    return [i*-7 for i in L if abs(i)>4]
