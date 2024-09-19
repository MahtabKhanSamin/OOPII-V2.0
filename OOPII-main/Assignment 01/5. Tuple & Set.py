books = (
("To Kill a Mockingbird", "Harper Lee", 1960),
("1984", "George Orwell", 1949),
("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)
tags = {"classic", "dystopian", "novel", "literature"}
print(books[1][1])
books=list(books)
books.append(['Brave New World','Aldous Huxley',1932])
books=tuple(books)
print(books)
#book=books[2]
(book1,book2,book3,book4)=books
print(book3)
for x in books:
    print(x[1])
tags.add('sci-fi')
print(tags)
tags.remove('novel')
print(tags)