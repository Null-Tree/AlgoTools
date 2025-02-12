import quicksort
import alexquicksort

import random


def mainsort(input:list):
###############################################
#please sort the input list and return the sorted list
        
    # quicksort.quickSort(unsortedList)
    # sortedList=unsortedList


    sortedList = alexquicksort.quicksort(input)
    
    return sortedList

###############################################




# CONFIG

# max lengh of list you wanna test
maxLengh=100

# what order to test for
# options: "asc" "desc" "either"
mode="either"



















################################################################################################################################################################################################

#sys











def checkorder(list:list, mode:str):
    if mode == "asc":
        for i in range(len(list)-1):
            if list[i] <= list[i+1]:
                continue
            else:
                return False

    elif mode == "desc":
        for i in range(len(list)-1):
            if list[i] >= list[i+1]:
                continue
            else:
                return False
    else:
        raise Exception("incorrect mode, either \"asc\" \"desc\" or \"either\" ")
    return True

def checkListContent(oldList:list,newlist:list):

    if len(oldList) != len(newlist):
        return False
    
    keys=[]
    oldDict={}
    newDict={}

    for i in oldList+newlist:
        if i not in keys:
            keys.append(i)
            oldDict[i]=0
            newDict[i]=0
    
    for i in oldList:
        oldDict[i]+=1

    for i in newlist:
        newDict[i]+=1
    
    for key in keys:
        if not (oldDict[key] == newDict[key]):
            print("mismatch values")
            return False
    
    return True
        

if __name__=="__main__":
    if maxLengh <1:
        raise Exception("please have maxLengh of 1 or heigher")

    for i in range(1,maxLengh+1):

        unsortedList=[]

        for j in range(i):

            unsortedList.append(random.randint(0,100))

        

        sortedList=mainsort(unsortedList.copy())


        print(f"Testing random list of lengh: {i}")
        passed = True

        # check order
        if mode == "either":
            if (not checkorder(sortedList,"asc")) and (not checkorder(sortedList,"desc")):
                print("incorrect order, accepting either order")
                print(f"input: {unsortedList}")
                print(f"received : {sortedList}")
                passed = False
        else:
            if (not checkorder(sortedList,mode)):
                print(f"incorrect order, testing for {mode} order")
                print(f"input: {unsortedList}")
                print(f"received : {sortedList}")
                passed = False
        

        if not checkListContent(sortedList,unsortedList):
            print(f"Contents of received list did not match original list")
            print(f"input: {unsortedList}")
            print(f"received : {sortedList}")
            passed = False

        
        if passed:
            print("Pass")
        else:
            print("No pass")
            quit()
    

    