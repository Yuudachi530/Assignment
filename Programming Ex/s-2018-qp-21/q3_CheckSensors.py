Temp = [40, 20, 40, 32, 47, 65, 43, 45, 34, 43]

LowTemp = 30
HighTemp = 50

def GetTemp(num):
    temp = Temp[num - 1]
    return temp

def Alarm():
    print('Warning!! High temperature!!')

def CheckSensors():
    while True:
        SensorID = int(input('enter the sensor ID: '))
        if 1 <= SensorID <= 10:
            break
        else:
            print()
            print('Invalid, please enter a number between 1 and 10')
    Temp = GetTemp(SensorID)
    if Temp < LowTemp:
        print()
        print('Cold')
    elif Temp > HighTemp:
        print()
        Alarm()
    else:
        print()
        print('Normal')

CheckSensors()
    