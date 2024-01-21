searched_book = input()
checked_books = 0

while True:
    book_name = input()
    if searched_book != book_name:
        checked_books += 1
    if book_name == 'No More Books':
        checked_books -= 1
        print(f'The book you search is not here!')
        print(f'You checked {checked_books} books.')
        break
    if searched_book == book_name:
        print(f'You checked {checked_books} books and found it.')
        break

