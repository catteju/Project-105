import csv
import math

with open('Data.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total + int(x)
    mean = total/n
    return mean

squaredList = []
for num in data : 
    a = int(num)-mean(data)
    a = a**2
    squaredList.append(a)

sum = 0
for i in squaredList:
    sum = sum + i

result = sum/(len(data) - 1)

std = math.sqrt(result)

print(std)