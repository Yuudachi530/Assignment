#procedure EggsIntoBoxes
def EggsIntoBoxes(NumberOfEggs):
    NumberOfBoxes = NumberOfEggs // 6
    EggsLeftOver = NumberOfEggs % 6
    print('Number of boxed filled: ', NumberOfBoxes)
    print('Number of eggs left: ', EggsLeftOver)
    
Eggs = int(input('enter the number of the eggs: '))
EggsIntoBoxes(Eggs)
    