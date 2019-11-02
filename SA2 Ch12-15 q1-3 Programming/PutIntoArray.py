file_holder = open('PRODUCTS.txt', 'r')
file_list = file_holder.readlines()
file_holder.close()
PCode = []
PDescription = []
PRetaiPrice = []

counter = 0
while True:
    PCode.append(file_list[counter])
    PDescription.append(file_list[counter + 1])
    PRetaiPrice.append(file_list[counter + 2])
    counter = counter + 3
    if counter == len(file_list) - 3:
        break
print('recording accomplished')
    
        
def ProductCodeSearch(PC):
    Counter = 0
    for i in PCode:
        if i == PC:
            return Counter
        Counter += 1
    if Counter == len(PCode):
        return -1





