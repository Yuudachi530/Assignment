#procedure OutputTimeTable
counter = 1
def OutputTimeTable(number):
    global counter
    if counter == number:
        product = counter * 5
        print(counter, '×', '5', '=', product)
    else:
        product = counter * 5
        print(counter, '×', '5', '=', product)
        counter = counter + 1
        OutputTimeTable(number)
        
Number = int(input('Enter a Number: '))
print()
OutputTimeTable(Number)