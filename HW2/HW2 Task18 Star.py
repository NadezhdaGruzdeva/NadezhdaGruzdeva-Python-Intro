# 18. *Реализуйте алгоритм перемешивания списка.
#Fill list  with unique random values
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

myList = [55, 6, 8, 31, 9, 303]

print (f'Mixed list is {ChengeOrderList(myList)}')




        
