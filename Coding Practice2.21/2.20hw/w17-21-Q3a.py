UserNameArray = ['' for i in range(99)]
print(UserNameArray)
def BubbleSort():
    for i in range(99):
        UserID = UserNameArray[i][:6]
        NextID = UserNameArray[i + 1][:6]
        if UserID > NextID:
            Temp = UserNameArray[i + 1]
            UserNameArray[i + 1] = UserNameArray[i]
            UserNameArray[i] = Temp
print(UserNameArray)
