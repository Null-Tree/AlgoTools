

def swap(list:list, i:int, j:int):
    list[i],list[j]=list[j],list[i]

def partition(input:list,iLow:int,iHigh:int,mode:str) -> int:
    oldPivotIndex = (iLow+iHigh)//2
    pivotValue = input[oldPivotIndex]

    # swaps the pivot number to the end of the list segment
    swap(input,oldPivotIndex,iHigh-1)

    i = iLow-1
    for j in range(iLow,iHigh-1):
        # checks if swapping is needed

        if mode == "asc":
            if input[j] < pivotValue:
                i+=1
                swap(input,j,i)
        elif mode == "desc":
            if input[j] > pivotValue:
                i+=1
                swap(input,j,i)

    
    # swaps the pivot number from its temporary spot to where it should be (i+1)
    newPivotIndex = i+1
    swap(input,newPivotIndex,iHigh-1)

    return newPivotIndex

# iLow and iHigh represent the indexes of the boundaries of the list segment to be partitioned
# note that the list is denoted by [ iLow : iHigh ), where number at index iHigh is not included
def quickSortRecursive(input:list,iLow:int,iHigh:int,mode:str):

    # Checks that the list has atleast 2 items to sort before it recurs
    if iLow<iHigh-1:
        pivot=partition(input,iLow,iHigh,mode)

        # use pivot +1 as pivot should be in right place, does not need to be sorted again
        quickSortRecursive(input,iLow,pivot,mode)
        quickSortRecursive(input,pivot+1,iHigh,mode)
        
def quickSort(input:list,mode:str):
    # initialises the recursion
    if mode not in ["asc","desc"]:
        raise Exception("Bad mode")
    quickSortRecursive(input,0,len(input),mode)

    




    