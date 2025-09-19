from models import Base, engine, Session, Author, Book

# Create tables
Base.metadata.create_all(engine)

# Open session
session = Session()

# Create Authors
author1 = Author(name="Chinua Achebe")
author2 = Author(name="Ngũgĩ wa Thiong’o")

# Create Books
book1 = Book(title="Things Fall Apart", author=author1)
book2 = Book(title="No Longer at Ease", author=author1)
book3 = Book(title="Petals of Blood", author=author2)
book4 = Book(title="The River Between", author=author2)

# Add to session
session.add_all([author1, author2, book1, book2, book3, book4])
session.commit()

# Query Authors and their Books
authors = session.query(Author).all()
for author in authors:
    print(f"Author: {author.name}")
    for book in author.books:
        print(f"   - {book.title}")

# Query Books and their Author
books = session.query(Book).all()
for book in books:
    print(f"Book: {book.title}, Author: {book.author.name}")
