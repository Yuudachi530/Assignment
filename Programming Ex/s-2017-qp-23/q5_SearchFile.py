LoginEvents = []

FileHolder = open('LoginFile.txt', 'r')
InfoHolder = FileHolder.readlines()
FileHolder.close()

def SearchFile():
    UserIDInput = input('enter the user ID: ')
    for i in InfoHolder:
        if i[:5] == UserIDInput:
            if i[-1:] == '\n':
                s = i[:-1]
                LoginInfo = [i[5:9], s]
            else:
                LoginInfo = [i[5:9], i[9:24]]
            LoginEvents.append(LoginInfo)

SearchFile()
print(LoginEvents)
            