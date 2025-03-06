


input = [1,5,2,3,5,3,67,1]

# MODE : "asc" or "desc"
def mergeSort(input:list, mode:str) -> list:
    lengh = len(input)
    if lengh <= 1:
        return input
    middle_index = lengh//2

    leftList=input[:middle_index]
    rightList=input[middle_index:]

    sortedLeftList = mergeSort(leftList,mode)
    sortedRightList = mergeSort(rightList,mode)
    
    lLengh = len(sortedLeftList)
    rLengh=len(sortedRightList)
    result=[]
    li,ri=0,0

    for i in range(lengh):
        if li >= lLengh:
            result.append(sortedRightList[ri])
            ri+=1
            continue
        if ri >= rLengh:
            result.append(sortedLeftList[li])
            li+=1
            continue

        # sort asending
        priority=""
        if mode =="asc":
            if sortedLeftList[li] > sortedRightList[ri]:
                priority = "r"
            else:
                priority="l"
        elif mode =="desc":
            if sortedLeftList[li] < sortedRightList[ri]:
                priority = "r"
            else:
                priority="l"



        if priority=="r":
            result.append(sortedRightList[ri])
            ri+=1
            continue
        else:
            result.append(sortedLeftList[li])
            li+=1
            continue


    return result





def main():
    print(mergeSort(input,"asc"))
    print(mergeSort(input,"desc"))


if __name__ == "__main__":
    main()