import quicksort
import alexquicksort

import random


def mainsort(input:list):
###############################################

#     please sort the input list and return the sorted list
        
    quicksort.quickSort(unsortedList)
    sortedList=unsortedList


    # sortedList = alexquicksort.quicksort(input)
    
    return sortedList
###############################################




# CONFIG

# max lengh of list you wanna test
maxLengh=100

# number of random lists to test per list lengh
trialsPerLengh = 3

# what order to test for
# options: "asc" "desc" "either"
mode="either"

# what time to test for, "real" or "process"
timerMode = "real"

















################################################################################################################################################################################################

#   #
 # #
  #
 # #
#   #

################################################################################################################################################################################################

#sys




import time

from datetime import timedelta




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

def printDebug(unsortedList,sortedList):
    print(f"input: {unsortedList}")
    print(f"received : {sortedList}")

if __name__=="__main__":
    if maxLengh <1:
        raise Exception("please have maxLengh of 1 or heigher")

    for i in range(1,maxLengh+1):
        for trial in range(trialsPerLengh):

            unsortedList=[]

            for j in range(i):

                unsortedList.append(random.randint(0,100))

            if timerMode== "real":
                Rstarttime=time.perf_counter()
                sortedList=mainsort(unsortedList.copy())
                Rendtime = time.perf_counter()
            elif timerMode == "process":
                Rstarttime=time.process_time()
                sortedList=mainsort(unsortedList.copy())
                Rendtime = time.process_time()
            else:
                raise Exception("invalid timer mode :(")
            
            RtimeTaken= timedelta(seconds=Rendtime - Rstarttime)

            print(f"Testing random list of lengh: {i}")
            print(f"    trial:{trial+1}")
            passed = True

            # check order
            if mode == "either":
                if (not checkorder(sortedList,"asc")) and (not checkorder(sortedList,"desc")):
                    print("incorrect order, accepting either order")
                    printDebug(unsortedList,sortedList)
                    passed = False
            else:
                if (not checkorder(sortedList,mode)):
                    print(f"incorrect order, testing for {mode} order")
                    printDebug(unsortedList,sortedList)
                    passed = False
            

            if not checkListContent(sortedList,unsortedList):
                print(f"Contents of received list did not match original list")
                printDebug(unsortedList,sortedList)
                passed = False

            print(f"    real time elapsed: {RtimeTaken}")
            if passed:
                print("    Pass")
            else:
                print("    No pass")
                quit()
        

    