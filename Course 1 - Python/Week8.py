from random import*
import math

#Problem 1

def summedOdds(L):
    result = 0
    for e in L:
        if (e%2==1):
            result = result + e
    return result

def untilARepeat(high):
    numguesses = 0    # we just made one, above
    L = []
    while uniq(L):
        guess = choice( range(0,high) )  # guess again!
        numguesses += 1  # add one to our number of guesses
        L = L+[guess]
    return numguesses


def uniq( L ):
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return uniq( L[1:] )


def dartThrow():
    x=uniform(-1,1)
    y=uniform(-1,1)
    return withinCircle(x,y)

def withinCircle(x,y):
    if math.sqrt(x**2 + y**2) < 1.0:
        return True
    else:
        return False

#---------------------
#Problem 2

def forPi(n):
    numthrows = 0
    numhits = 0
    piVal = 0 

    for i in range(n):
        numthrows+=1
        if dartThrow():
            numhits+=1
        piVal = 4.0 * numhits/numthrows
        print str(numhits) + " hits out of " + str(numthrows) + " throws so that pi is " + str(piVal)
        
    return piVal

def whilePi(maxerror):
    numthrows = 0
    numhits = 0
    piVal = 0

    while (abs(math.pi - piVal) > maxerror):
        numthrows+=1
        if dartThrow():
            numhits+=1
        piVal = 4.0 * numhits/numthrows
        print str(numhits) + " hits out of " + str(numthrows) + " throws so that pi is " + str(piVal)

    return numthrows


#---------------------
#Problem 3

def menu():
    """ a function that simply prints the menu """
    print
    print "(0) Input a new list"
    print "(1) Print the current list"
    print "(2) Find the average price"
    print "(3) Find the standard deviation"
    print "(4) Find the min and its day"
    print "(5) Find the max and its day"
    print "(6) Your TT investment plan"
    print "(9) Quit"
    print 

def predict(L):
    """ predict ignores its input and returns
        what the next element should have been
    """
    return 42.0

def main():
    """ the main user-interaction loop """

    L = [] # an initial list

    while True:   # the user-interaction loop
        menu()
        print
        uc = raw_input( "Enter your choice: " )

        if uc == '9': # we want to quit
            break

        elif uc == '0':
            new_list = input("Enter a new list of prices: ")
            L = new_list

        elif uc == '1': # we want to enter a new list
            print "Day   Price"
            print "---   -----"
            for i in range(len(L)):
                print " " + str(i) + "     " + str(L[i])

        elif uc == '2': # predict and add the next element
            average = calcAverage(L)
            print "The average price is " + str(average)

        elif uc == '3':
            sd = calcSD(L)
            print "The st. deviation is " + str(sd)

        elif uc == '4':
            indexMin = 0
            minVal = calcMin(L, indexMin)
            print "The min is " + str(minVal[0]) + " on day " + str(minVal[1])

        elif uc == '5':
            indexMax = 0
            maxVal = calcMax(L, indexMax)
            print "The max is " + str(maxVal[0]) + " on day " + str(maxVal[1])

        elif uc == '6':
            maxVal = calcMax(L)
            minVal = calcMin(L)
            print "Buy on day " + str(minVal[1]) + " at price " + str(minVal[0])
            print "Sell on day " + str(maxVal[1]) + " at price " + str(maxVal[0])
            print
            profit = maxVal[0] - minVal[0]
            print "For a total profit of " + str(profit)
            
        else:
            print "The choice " + str(uc) + " is not an option."
            print "Try again!"

    print
    print "See you yesterday!"


def calcAverage(L):
    sum = 0
    for i in L:
        sum+=i
    return float(sum/len(L))

def calcSD(L):
    sumOfSqrs = 0
    avgVal = float(calcAverage(L))
    for i in L:
        sumOfSqrs+=float((i-avgVal)**2)
    return math.sqrt(sumOfSqrs/len(L))

def calcMin(L, indexMin = 0):
    minVal = L[0]
    for i in range(len(L)):
        if L[i] < minVal:
            minVal = L[i]
            indexMin = i
    return [minVal, indexMin]

def calcMax(L, indexMax = 0):
    maxVal = L[0]
    for i in range(len(L)):
        if L[i] > maxVal:
            maxVal = L[i]
            indexMax = i
    return [maxVal, indexMax]


#---------------------












#---------------------

def minday(L):
    minval = L[0]
    minday = 0
    for i in range(len(L)):
        if L[i] < minval:
            minval = L[i]
            minday = i
    return [minday, minval]


def menu():
    print "(1) Enter the event name"
    print "(2) Enter a new attendee"
    print "(3) Show current attendees"
    print "(4) Quit"
    print

##def main():
##    event_name = "Default Event"
##    attendees = []
##    while True:
##        print "\nThe event is", event_name, "."
##        menu()
##        uc = input("Choose an option: ")
##
##        if uc == 4:
##            break
##        elif uc == 1:
##            event_name = raw_input("Enter the event name: ")
##        elif uc == 2:
##            attendee_name = raw_input("Enter the attendees name: ")
##            attendees.append(attendee_name)
##            print "\n", attendee_name, "has been added to the list of attendees."
##        elif uc == 3:
##            print "\nThe list of attendees for", event_name, "is: ", attendees, "."
##        else:
##            print "\nThats not on the menu!"
##
##    print
##    print "You have quit the program"


def print_list():
    L = [0,1,2,3,4,5]

    for i in L:
        print i

    return

def recursive_fac(N):
    if N == 0:
        return 1
    else:
        return N * recursive_fac(N-1)

def for_fac(N):
    result = 1
    for i in range(1,N+1):
        result = result*i
    return result

def recursive_power(b, p):
    if p==0:
        return 1
    elif p<0:
        return 1.0/b * recursive_power(b,p+1)
    else:
        return b*recursive_power(b,p-1)

def for_power(b, p):
    answer=1

    for i in range(abs(p)):
        answer=b*answer

    if p<0:
        return 1.0/answer
    else:
        return answer


def whilLoopFac(n):
    answer = 1
    while n>0:
        answer = answer*n
        n-=1
    return answer


def randomGuess(level,max):

    if max==0:
        print "YOU WIN!!!"
        return
    
    randNum = choice(range(0,max+1))
    n = -1
    counter = level
    lives = 3
    print
    print "Max value is " + str(max)
    print "You have 3 lives"
    
    while (n!=randNum):
        print "You have " + str(counter) + " chances"
        
        if (counter == 0):
            counter = level
            lives = lives-1

            if lives == 0:
                print
                print "YOU LOSE"
                return
            
            print "Answer was " + str(randNum)
            print 
            print "Counter Reset"
            print "You have " + str(lives) + " lives"
            print "You have " + str(counter) + " chances"
            randNum = choice(range(0,max+1))
            
        counter-=1

        n = int(input("Guess a number: "))
        
        if (n>randNum):
            print "Too high"
        if (n<randNum):
            print "Too low"

    print "You got it"
    return randomGuess(level-1, max-20)
    

def roll():
    return choice(range(1,7))

def rollMany(n):
    return sum([roll() for x in range(n)])

def odds(goal, n, trials):
    rolls = [rollMany(n) for i in range(trials)]
    successes = [1 for roll in rolls if roll == goal]
    return len(successes)/float(trials)

def calculateSecInHour():
    secondsInHour = 0
    minutesInHour = 60
    secondsInMinute = 60
    for i in range(minutesInHour):
        for i in range(secondsInMinute):
            secondsInHour += 1
    return secondsInHour
