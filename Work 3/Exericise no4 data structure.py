#stack questions

stack=[]
stack.append("Read Notes")
stack.append("Do Practice")
stack.append("Take Exam")
print("the stack is:",stack)
stack.pop()
stack.pop()
print("the remaining item in stack is:",stack)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
irembo=[]
irembo.append("Enter Details")
irembo.append("Upload Id")
irembo.append("Confirm")
print("the irembo is:",irembo)
irembo.pop()
print("the steps remain in irembo is:",irembo)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#Queue question1

from collections import deque
queue1=deque(["Bus1","Bus2","Bus3","Bus4","Bus5","Bus6","Bus7","Bus8"])
print("queue1:",queue1)
i=1
for i in range(5):
    queue1.popleft()
print("The front Bus now is:",queue1[0])
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
queue2=deque(["customer1","customer2","customer3","customer4"])
print("queue2:",queue2)
queue2.popleft()
print("the customer to be served second is:",queue2[0])
