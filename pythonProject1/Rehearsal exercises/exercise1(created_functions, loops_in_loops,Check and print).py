def read_books():
    with open('Files Chapter 12/books.txt') as file:
        books_list = []
        line = file.readline().rstrip()
        while line:
            books_list.append(line)
            line = file.readline().rstrip()
    return books_list

def menu():
    user_input = input('a - Overview\nb - Longest title\nc - 5 letter on a row\ns - Stop\nMake your choice: ')
    while user_input.upper() not in ('A','B','C','S'):
        user_input = input('a - Overview\nb - Longest title\nc - 5 letter on a row\ns - Stop\nMake your choice: ')
    return user_input



def print_list(books):
    print('List of books:\n')
    counter = 0
    for i in range(len(books)):
        counter = counter + 1
        print(counter, books[i])


books = read_books()
return_selection = menu()
while return_selection:
    if return_selection.upper() == 'A':
        print_list(books)
        print()
        return_selection = menu()
    if return_selection.upper() == 'B':
        print_list(books)
        longest_title = max(books,key=len)
        longest_title_no = len(longest_title)
        print('The length of the longest title has', longest_title_no, 'characters', '\n')
        return_selection = menu()
    if return_selection.upper() == 'C':
        #  Print 5 elements at a time
        booknumber = int(input('Enter booknumber max 10: '))
        selected_book = (books[booknumber-1])
        for i in range(0, len(selected_book), 5):  # characters in line start 0 to the end, take 5 at a time
            five_list = selected_book[i:i+5]
            print(five_list,sep=' ')
        print()
        return_selection = menu()
    else:
        break



