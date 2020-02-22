FileHolder = open('BookInfo.txt','r',encoding='UTF-8')
BookInfoList = FileHolder.readlines()
FileHolder.close()
Num = 1
BookInfoList_New = []
for i in BookInfoList:
    Index = 0
    for j in i:
        if j == ',':
            AuthorName = i[:Index]
            BookTitle = i[Index + 1:-2]
            break
        else:
            Index = Index + 1
    if Num < 10:
        SNum = '#' + '0' + str(Num)
    else:
        SNum = '#' + str(Num)
    Index2 = 0
    for x in AuthorName:
        if x == ' ':
            NumOfCopy = str(ord(AuthorName[Index2 + 1]))
    BookInfoList_New.append([SNum,AuthorName,BookTitle,NumOfCopy])
    Num = Num + 1

def AddNewBook(authorname,booktitle,numofcopy):
    BookInfoList_New.append(['#' + str(len(BookInfoList_New)),authorname,booktitle,numofcopy])

while True:
    print('Add a new book to the text file, press 1 Search for books written by a given author, press 2 End the program, press 3')
    Judge = int(input('User: '))
    if Judge == 1:
        AuthorName = input('Enter the authorname: ')
        BookTitle = input('Enter the booktitle: ')
        NumOfCopy = input('Enter the NumOfCopy: ')
        AddNewBook(AuthorName, BookTitle, NumOfCopy)
        break
    elif Judge == 2:
        Search = input('enter the book title: ')
        for i in BookInfoList_New:
            if i[1] == Search:
                print(i)
        break
    elif Judge == 3:
        break
    else:
        print('invalid, please try it again.')

FileHolder = open('BookInfo_New.txt','w')
FileHolder.writelines(BookInfoList_New)
       


