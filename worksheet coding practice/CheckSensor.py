ID_dic = {}
LowTemp = -10
HighTemp = 50

def Alarm():
    print('Warning!')


def GetTemp(SencorID):
    Temp = ID_dic[SencorID]
    return Temp
     
def CheckSensor():
    SencorID = int(input('enter the sencor ID: '))
    while 1 <= SencorID <= 10:
        Temp = GetTemp
        if Temp < LowTemp:
            print('Cold')
        elif Temp > HighTemp:
            Alarm()
        else:
            print('Normal')
CheckSensor()
    