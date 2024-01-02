import ebook

book = ebook.Ebook('Harry Potter','J.K. Rowling', 465)

book.open()

book.status()

for i in range(5):
    book.read()

book.status()

book.close()

for i in range(10):
    book.read()

