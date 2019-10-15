FileHolder = open('StudentContact.txt', 'r')
List_StudentContact = FileHolder.readlines()
FileHolder.close()
FileHolder = open('ClassList.txt', 'r')
List_ClassList = FileHolder.readlines()
FileHolder.close()


def SearchFile():
    for line in List_StudentContact():
        counter = 0
        for i in line:
            if i == '*':
                name = line[:counter]
                if Name == name:
                    return line
            counter = counter + 1
    return ''

def
    
            
            
    








