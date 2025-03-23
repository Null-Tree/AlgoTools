def b(l,i):
    if i >10:
        return 
    l.append(len(l))
    print(f"b {l}")
    i+=1
    b(l,i)

def a():
    l=[]
    b(l,1)

a()