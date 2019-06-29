book = "hellow python hellow world"
book_search_library = book.split()
number_word_notRecommended = int(input("please enter the number of word(s) that is not recommend for a child to read: "))
list_word_notRecommended = []

output_list_book = []

for i in range(number_word_notRecommended):
    word_notRecommended = str(input("please enter each word: "))
    list_word_notRecommended.append(word_notRecommended)

def book_recommend(book, notRecommended):
    for i in notRecommended:
        for x in book:
            if i == x:
                book.remove(i)
    return book

print(book_recommend(book_search_library, list_word_notRecommended)) 
    
        
            
    
                
        
    
    
    
