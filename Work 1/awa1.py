#insurance claims Queque
#integer
from array import array
claims=[200,10,30,90,130,140]
total_claims=round(sum(claims))
avg_claims=round(total_claims/len(claims))
max_claims=round(max(claims))
min_claims=round(min(claims))
print("total claims marks are:",total_claims)
print("average claims marks are:",avg_claims)
print("max claims marks are:",max_claims)
print("min claims marks are:",min_claims)

#string
claims=[200,10,30,90,130,140]
total_claims=round(sum(claims))
avg_claims=round(total_claims/len(claims))
print("The number of claims marks are:",len(claims))
print("total claims marks are:",total_claims)
print("average claims marks are:",avg_claims)

#boolean
claims=[200,10,30,90,130,140]
threshold=100
c=1
for c in claims:
    if c >= threshold:
        print(f"the claims{c} is: Above Standard")
    else:
        print(f"the claims{c} is: Below Standard")
#list
claims=[200,10,90,130,30,140]
print("This is the list before any operation:",claims)
claims.append(50)
claims.append(70)
c=1
for c in claims:
    if c >=101:
        claims.remove(c)
print("This is the list after any operation:",claims)
claims.sort()
print("The final list after sorting:",claims)

#arrays
claims=[200,10,90,130,30,140]
arr=(10,200,140)
print("array data:",arr)
array_sum=sum(arr)
list_sum=sum(claims)
print(f"array sum is {array_sum}")
print(f"list_sum is {list_sum}")
if array_sum==list_sum:
    print("array sum equals list_sum")
else:
    print("array sum does not equal list_sum")

#dictiontary
record1=[{"id": 1, "name": "Claim1", "value": 120},
         {"id": 2, "name": "Claim2", "value": 90},
         {"id": 3, "name": "Claim3", "value": 80},]
record1[1]["value"]=100 #update record
record1.pop(0) #remove record
total_value=sum(r["value"] for r in record1)
print("Total value across records:",total_value)
avg_value=total_value/len(record1)
if avg_value>120 and len(record1)>=2:
    print("the average value is Above Standard")
else:
    print("the average value is Below Standard")


