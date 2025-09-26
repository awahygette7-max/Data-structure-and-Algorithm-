#stack question

stack1=[] #Defining the name of the stack
stack1.extend(["1","2","3"]) #push items in the stack
stack1.pop() #removing "3" from the stack
stack1.append("4") #pushing into the stack another item
print("The top item is:",stack1[-1]) #displaying the item on the top of the stack by using itlocation in stack
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#Queue question
#Queue vs Stack for stadium entry. which is fair
from collections import deque
#Queue use fair method as follows
arrivals=["Awa","Tete","Olla","Ella","Bob"]
queue1=[]
queue1 = deque()
for person in arrivals:
    queue1.append(person) # we use iteration to add person at the back of the line as they arrive
#serving people as they have arrived
queue1_served=[]
while queue1:
    nextperson=queue1.popleft() #to remove person from the front as he/she arrived first
    queue1_served.append(nextperson)
print("queue method of serving :",queue1_served) #this shows that if you arrive first you have to be served first to be fair

#stack method is unfair for this
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
stack1=[] # decralaration of new set of items
for person in arrivals:
    stack1.append(person) # add each person to the stack as they arrived at the stadium at th top of the stack
#serving peoples
stack1_served=[]
while stack1:
    nextperson=stack1.pop() #to remove person from the top as the last person to be add to the stack
    stack1_served.append(nextperson)
print("stack method of serving:",stack1_served) #this shows you entered last nd you be served first which is not fair for the ones who arrived at the stadium earlier and have been waiting for so long


