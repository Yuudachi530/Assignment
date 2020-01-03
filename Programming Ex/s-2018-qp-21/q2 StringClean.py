def StringClean(InString):
    OutString = ''
    for Counter in range(len(InString)):
        NextChar = InString[Counter]
        if 'A' <= NextChar <= 'Z':
            NextChar = chr(ord(NextChar) + 32)
            OutString = OutString + NextChar
        elif 'a' <= NextChar <= 'z':
            OutString = OutString + NextChar
    return OutString

print(StringClean('ANDJKSA_,sakicojJDskjabsdkajANsd'))
            
            
        
