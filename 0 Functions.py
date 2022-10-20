def FillUniqueRand(N):
    """"
    Fill list with unique random values.
    Size of list is entered by user.
    """
    import random
    myList = []
    for i in range (0,N):
        myList.append(0)
    
    isUnique = True
    myList[0] = random.randint(1, N)
    i = 1
    myCounter = 1
    while i in range (1, N):
        myList[i] = random.randint(1, N)
        for j in range(0, myCounter):
            if myList[j] == myList[i]:
                isUnique = False
                break
            else:
                isUnique = True
        if isUnique == False:
            continue
        else:
            i += 1
            myCounter += 1
    return(myList)

def ChengeOrderList(yourList = []):
    """
    Change order of element in the mentioned list by creating new list.
    """
    mixedList = []
    sizeYourList = len(yourList)
    newOrder = (FillUniqueRand(sizeYourList))
    print(f'New order is {newOrder}')
    for i in range(0, sizeYourList):
        ind = newOrder[i]-1
        mixedList.append(yourList[ind])
    return mixedList

def SumFiguresOfRealEnteredNumber ():
    number = float(input('Enter the real number \n'))
    numberStr = str(number)
    figuresOnlyStr = numberStr.replace('.','')
    figuresOnlyStr = figuresOnlyStr.replace('-','')
    figuresQty = len(figuresOnlyStr)
    figuresSum = 0
    for i in range(figuresQty):
        figuresSum += int(figuresOnlyStr[i])
    print(f'Figures sum of entered number = {figuresSum}')

def MultiplFibanachi():
    N = int(input('Enter the number \n'))
    multiplList = []
    valueMultiplList = 1
    if N > 0:
        for i in range (N):
            valueMultiplList *= (i + 1)
            multiplList.append(valueMultiplList)
    
    else:
        for i in range(1, N - 1, -1):
            multiplList.append(valueMultiplList)
            valueMultiplList *= (i - 1)
    print(multiplList)   

def SpecDict():
    n = int(input('Enter the number \n'))
    dictForSequence = {}
    for i in range (1, n + 1):
        dictForSequence[i] = round((1 + 1 / i) ** i, 2)
    print(dictForSequence)

def CreateListFromNegatToPositive(N):
    myList = []
    indexForMyList = 0
    if N > 0:
        for i in range (-N, N + 1):
            myList.append(i)
            indexForMyList += 1
    else:
        for i in range(-N, N - 1, -1):
            myList.append(i)
            indexForMyList -= 1
    return(myList)   