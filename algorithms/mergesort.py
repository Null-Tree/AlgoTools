


input = [1,5,2,3,5,3,67,1]

n=0


def sort(input:list) -> list:
    print(n)
    n+=1
    lengh = len(input)
    if lengh <= 1:
        return list
    
    middle_index = lengh//2

    leftList=input[:middle_index]
    rightList=input[middle_index:]

    print(f"""
    r:
    {rightList}
    l:
    {leftList}
    
    """)
    sortedLeftList = sort(leftList)
    sortedRightList = sort(rightList)
    
    lLengh = len(sortedLeftList)
    rLengh=len(sortedRightList)
    result=[]
    li,ri=0

    for i in lengh:
        
        if li >= lLengh:
            result.append(sortedRightList[i])
            ri+=1
        if ri >= rLengh:
            result.append(sortedLeftList[i])
            li+=1

        # sort asending
        if sortedLeftList[i] > sortedRightList[i]:
            result.append(sortedRightList[i])
            ri+=1
        else:
            result.append(sortedLeftList[i])
            li+=1

    return result





def main():
    lst=sort(input)
    print(lst)



main()