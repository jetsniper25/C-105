import csv 
import math

with open("data.csv", newline="")as f:
    reader=csv.reader(f)
    fileData=list(reader)
 
data=fileData[0]

def mean(data):
    totalMarks=0
    totalEntries=len(data)

    for marks in data:
        totalMarks+=int(marks)

    mean=totalMarks/totalEntries
    print(mean)
    return mean

squaredList=[]
for n in data:
    a=int(n)-mean(data)
    a=a**2
    squaredList.append(a)

sum=0
for i in squaredList:
    sum=sum+i

result=sum/(len(data)-1)
stdev=math.sqrt(result)
print(stdev)
