import random

NumList = []
for i in range(20):
    num = random.randint(0, 20)
    NumList.append(num)
for i in range(20):
    num = random.randint(0, 40)
    NumList.append(num)

TotalValue = 0
ZeroCount= 0

for Num in NumList:
    TotalValue = TotalValue + Num
    if Num == 0:
        ZeroCount = ZeroCount + 1

print('Average:', TotalValue / 100)
print('Number of zero:', ZeroCount)








