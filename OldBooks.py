search_book = input()
count_books = 0
while True:
    book = input()
    if book == search_book:
        print(f'You checked {count_books} books and found it.')
        break
    if book == "No More Books":
        print(f'The book you search is not here!')
        print(f'You checked {count_books} books.')
        break
    count_books += 1
    