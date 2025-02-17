def quicksort(listToSort: list) -> list:
    if len(listToSort) <= 1:
        return listToSort
    pivot = len(listToSort) // 2
    i = 0
    while i < len(listToSort):
        if i == pivot:
            i += 1
            continue
        
        item = listToSort[i]
        pivotItem = listToSort[pivot]

        if item < pivotItem and i > pivot:
            listToSort.insert(pivot, listToSort.pop(i))
            pivot += 1
        elif item > pivotItem and i < pivot:
            listToSort.insert(pivot, listToSort.pop(i))
            pivot -= 1
            i -= 1
        i += 1
    return quicksort(listToSort[:pivot]) + [pivotItem] + quicksort(listToSort[pivot+1:])