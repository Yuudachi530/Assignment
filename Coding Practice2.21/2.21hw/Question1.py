FileHolder = open('BookInfo.txt','r',encoding='UTF-8')
BookInfoList = FileHolder.readlines()
FileHolder.close()
Num = 1
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
    print(SNum + ' ' + 'Book Author: ' + AuthorName + 'Book Title:' + BookTitle)
    Num = Num + 1
        
