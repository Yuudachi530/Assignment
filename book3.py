file_book = open("Alice's Adventures in wonderland","r")
file_word = open("vocabulary file","r")
file_book = file_book.readlines()
list_file_book = []
for line in file_book:
    list_file_book.append(line.split())
    
def search_linear(list_library_1, string_target):
    for i in list_library_1:
        if i == string_target:
            return True
        else:
            return False
output_list_notrecommended = []

def search_word_notrecommended(list_library_1,list_library_2):
    for x in list_library_2:
        if search_linear(list_library_1, x) != True:
            output_list_notrecommended.append(x)
    return output_list_notrecommended

            
            
print(search_word_notrecommended(list_file_book, file_word))