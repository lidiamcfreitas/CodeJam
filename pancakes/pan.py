dividePrice = 0

def countMaximums(initInput):
    maxi = initInput[0]
    cm = 1
    l = len(initInput)
    while (cm < l and initInput[cm] == maxi):
        cm += 1
    return int(maxi), cm

def calculateNextCost(initInput, maximum, cm):
    global dividePrice
    dividePrice += cm
    
    l = len(initInput)
    
    if maximum %2 == 0:
        nextMax = maximum //2
    else:
        nextMax = maximum //2 + 1
    
    if l-1 > cm:
        a = initInput[cm+1]
        if a > nextMax:
            nextMax = a
    
    return dividePrice + nextMax

def newInput(initInput, maximum, cm):
    inputWithoutMax = initInput[cm:]
    if (maximum%2==0):
        return inputWithoutMax + [maximum//2]*2*cm
    else:
        return inputWithoutMax + ([maximum//2+1]+[maximum//2])*cm

def minimumCost(initInput,t, result):
    global dividePrice

    initInput.sort(reverse = True)
    maximum, cm = countMaximums(initInput)
    currentCost = maximum + dividePrice
    
    nextCost = calculateNextCost(initInput, maximum, cm)

    if (nextCost >= currentCost):
        print("Case #%d: %d" %(t, currentCost))
        return currentCost
    else:
        minimumCost(newInput(initInput, maximum, cm), t)
    return currentCost


# MAIN 

T = int(raw_input())
for test in range(1,T+1):
    dividePrice = 0
    result = 0
    D = int(raw_input())
    initInput = map(int, raw_input().split(" "))
    # print(initInput) # [11, 1, 7, 9]
    minimumCost(initInput, test, result)