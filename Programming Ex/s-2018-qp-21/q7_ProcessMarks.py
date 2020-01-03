import random

Mark = []

for i in range(20):
    Num = random.randint(1, 50)
    Mark.append(Num)
    
def ProcessMarks():
    Sum = 0
    for j in Mark:
        Sum = Sum + j
    MaxNum = max(Mark)
    Average = Sum // len(Mark)
    return 'the highest score is:', MaxNum, 'the average is:', Average

    
    