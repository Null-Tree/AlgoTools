


mainlist=[1,2,3,4,5]
# mainlist=[1,2,3,4]
out=[]

lstrange=list(range(len(mainlist)))

# order matter
# for i in lstrange:
#     for j in lstrange:
#         for k in lstrange:
#             if i==j or j==k or i==k:
#                 continue
#             out.append([mainlist[i],mainlist[j],mainlist[k]])

has=[]

# order no matter
for i in lstrange:
    for j in lstrange:
        for k in lstrange:
            if i==j or j==k or i==k:
                continue
            indexlist=[i,j,k]
            indexlist.sort()
            indexstring=""
            for index in indexlist:
                indexstring+=(str(index)+".")
            

            if indexstring in has:
                continue
            else:
                has.append(indexstring)
                out.append([mainlist[i],mainlist[j],mainlist[k]])


print()
print(has)
print()

for item in out:
    print(f"({item[0]} {item[1]} {item[2]})" , end=" ")