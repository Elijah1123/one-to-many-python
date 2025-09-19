from models import Base, engine, Session, Author, Book

# Create tables if they don’t exist
Base.metadata.create_all(engine)

session = Session()

def add_author():
    name = input("Enter author name: ")
    author = Author(name=name)
    session.add(author)
    session.commit()
    print(f"✅ Author '{name}' added.")

def add_book():
    authors = session.query(Author).all()
    if not authors:
        print("⚠️ No authors found. Please add an author first.")
        return
    
    print("Available Authors:")
    for author in authors:
        print(f"{author.id}: {author.name}")
    
    author_id = int(input("Enter author ID for this book: "))
    title = input("Enter book title: ")

    book = Book(title=title, author_id=author_id)
    session.add(book)
    session.commit()
    print(f"✅ Book '{title}' added to author ID {author_id}.")

def list_authors():
    authors = session.query(Author).all()
    if not authors:
        print("⚠️ No authors found.")
        return

    for author in authors:
        print(f"Author: {author.name}")
        for book in author.books:
            print(f"   - {book.title}")

def list_books():
    books = session.query(Book).all()
    if not books:
        print("⚠️ No books found.")
        return

    for book in books:
        print(f"Book: {book.title}, Author: {book.author.name}")

def main():
    while True:
        print("\n📚 One-to-Many CLI App")
        print("1. Add Author")
        print("2. Add Book")
        print("3. List Authors and Books")
        print("4. List Books and Authors")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_author()
        elif choice == "2":
            add_book()
        elif choice == "3":
            list_authors()
        elif choice == "4":
            list_books()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
