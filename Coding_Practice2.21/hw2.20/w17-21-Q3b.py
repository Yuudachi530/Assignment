UserNameArray = ['' for i in range(100)]

def FindRepeats():
    RepeatCount = 0
    for i in range(1, 100 + 1):
        FirstID = UserNameArray[i - 1][:6]
        SecondID = UserNameArray[i][:6]
        if FirstID == SecondID:
            RepeatCount = RepeatCount + 1
            print(UserNameArray[i])
        
    if RepeatCount == 0:
        print('the array contains no repeat counts')
        print('there are' + RepeatCount + 'repeated UserIDs')