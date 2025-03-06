

def lstcmp(l1:list,l2:list):
    # print(f"compare {l1}   {l2}")
    if len(l1) == len(l2):
        n = len(l1)
        for i in range(n):
            if l1[i] == l2[i]:
                continue
            else:
                return False
        
        return True
    else:
        raise Exception()


n=7
Lqueue = []

for i in range(n,0,-1):
    Lqueue.append(i)

# [5,3,2,1,]

results=[]
methods = []

def recur(inlist:list,spur:list,out:list,meth:list):
    if len(inlist + spur) == 0:
        global results
        results.append(out)
        methods.append(meth)
    
    # copy

    cinlist = inlist.copy()
    cspur = spur.copy()
    cout=out.copy() 
    
    # actions: spur-> end, in to end, in to spur
    #  take from start take from  start
    
    if len(inlist) != 0:
        # in to end
        
        recur(cinlist[1:],cspur,[cinlist[0]]+cout, meth + [f"{cinlist[0]} in to end"])


        # in to spur  add to fround of spur
        recur(cinlist[1:],[cinlist[0]]+cspur,cout, meth + [f"{cinlist[0]} in to spur"])
    

    if len(spur) !=0:
        recur(cinlist,cspur[1:],[cspur[0]]+cout,  meth + [f" {cspur[0]} spur to end"])
        

    



recur(Lqueue,[],[],[])
print(Lqueue)



print("================")
print(Lqueue)
print("================")

uniqueResults=[]
uniqueMeth = []

index=0
for lst in results:
    
    result=lst
    notIn=True
    for uniqueResult in uniqueResults:
        if lstcmp(result,uniqueResult):
            notIn = False
            # print(f"not unique : {result}")
            break
    if notIn:
        uniqueResults.append(lst)
        # found unique sol
        print(result)
        print(methods[index])
    


    index+=1



print(len(uniqueResults))