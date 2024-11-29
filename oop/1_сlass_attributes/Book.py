class Book:
    name = '1984'
    writer = 'Джордж Оруэлл'
    pages = 213

print(Book.writer)
print(Book.name)

print(getattr(Book, "writer"))
print(getattr(Book, "pages"))

setattr(Book, 'name', "Скотный двор")
setattr(Book, 'pages', 115)

setattr(Book, 'rating', 8.7)
Book.genre = "dystopian"

del Book.pages
delattr(Book, 'writer')
del Book.rating

print(Book.__dict__)