from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # One-to-many: Author -> Books
    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"<Author(name={self.name})>"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    # Many-to-one: Book -> Author
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author.name})>"


# Database setup
engine = create_engine("sqlite:///database.db", echo=True)
Session = sessionmaker(bind=engine)
