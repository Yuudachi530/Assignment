def AddNewScores():
    FileHolder =  open('ScoreDetails.txt', 'w')
    LineHolder = []
    while True:
        while True:
            Date = input('enter date in the form DDMMYY: ')
            if len(Date) == 6:
                break
            else:
                print()
                print('Invalid Date')
        while True:
            MembershipNumber = input('enter 4-digit membership number: ')
            if len(MembershipNumber) == 4:
                break
            elif MembershipNumber == '':
                break
            else:
                print()
                print('Invalid MembershipNumber')
        if MembershipNumber == '':
            break
        while True:
            Score = int(input('enter the score, range from 50 to 99: '))
            if 50 <= Score <= 99 and len(str(Score)) == 2:
                Score = str(Score)
                break
            else:
                print()
                print('Invalid Score')
        Line = MembershipNumber + ' ' + Date + ' ' + Score + '\n'
        LineHolder.append(Line)
    for line in LineHolder:
        FileHolder.write(line)
    FileHolder.close()

AddNewScores()
        
        
            
            
        