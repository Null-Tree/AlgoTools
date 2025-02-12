from quicksort import *

import random
if __name__=="__main__":
    
    print("##################################################################################")
    for i in range(1,10):
        newlist=[]
        for j in range(i):
            newlist.append(random.randint(0,100))
        
        print(f"sort: {newlist}")
        quickSort(newlist)
        
        print("----------------------------------------------------------------------------------")
        print(f"sorted{newlist}")
        print("##################################################################################")

    

    