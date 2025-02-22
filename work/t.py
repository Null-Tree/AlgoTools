
# orders will be stored as follows


def order(itemlist, otherpriority):
  lst=[itemlist,otherpriority*len(itemlist)]
  return lst

class orders:
  def __init__(self):
    orders.orderlist=[]
    
  def newOrder(self,itemlist,otherpriority):
    self.orderlist.append(order(itemlist,otherpriority))
  
  def getOrder(self):
    if len(self.orderlist)==0:
      return None
    
    min = self.orderlist[0][1]
    index=0
    for i in range(1,len(self.orderlist)):
      order = self.orderlist[i]
      if order[1]<min:
        index=i

    minOrder = self.orderlist[index][0].copy()
    self.orderlist.pop(index)


    return minOrder
    
    
    

db=orders()

# in this implementation, the the lower the number the higher the priority
# priority is multiplied with items in the order to get final priority

db.newOrder(["bananas","mangoes","bottles"],3)
db.newOrder(["mangoes","bottles"],2)
db.newOrder(["rats","flour","chips"],8)

print(db.getOrder())
print(db.getOrder())
print(db.getOrder())







