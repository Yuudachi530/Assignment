m = int(input('Enter the original scale: '))
n = int(input('Converse to the scale of: '))

base = input('Enter the original base: ')

OverHex = ['A','B','C','D','E','F']
OverHex_Num = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

def Converse_10(Base):
    if m < 10:
        Sum = 0
        Base_Len = len(Base)
        for Num in Base:
            Value = m**(Base_Len - 1) * int(Num)
            Sum = Sum + Value
            Base_Len  = Base_Len - 1
        return Sum
    elif 10 <= m <= 16:
        Sum = 0
        BaseList = []
        for j in Base:
            BaseList.append(j)
        Base_Len = len(BaseList)
        Index = 0
        while Index <= Base_Len - 1:
            for Item in OverHex:
                if Item == BaseList[Index]:
                    BaseList[Index] = OverHex_Num[Item]
            Index = Index + 1
        for i in BaseList:
            Value = m**(Base_Len - 1) * int(i)
            Sum = Sum + Value
            Base_Len = Base_Len - 1
        return Sum
    else:
        return 'ERROR: The original scale is out of range(16)'

list1 = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def Converse_n(DecimalNum):
    Output = ''
    Dividend = DecimalNum
    while True:
        Quotient = Dividend // n
        Remainder = Dividend % n
        Output = Output + list1[Remainder]
        Dividend = Quotient
        if Quotient == 0:
            Output = Output[::-1]
            break
    return Output

decimal = Converse_10(base)
print(decimal)
print('output:', Converse_n(decimal))









                

