# one-to-many-python

One-to-Many Relationship Project (Python + SQLAlchemy)

This project demonstrates a One-to-Many relationship using Python and SQLAlchemy.
We use the real-world example of Authors (one) → Books (many).

One Author can write many Books

Each Book belongs to exactly one Author

It includes a CLI (Command-Line Interface) to add authors, add books, and list relationships interactively.

🚀 Features

Add authors

Add books (linked to an author)

List all authors with their books

List all books with their authors

SQLite database storage

Fully object-oriented using SQLAlchemy ORM

🛠 Requirements

Make sure you have Python 3.9+ installed.

Install dependencies:

pip install sqlalchemy


(Optional for PostgreSQL / MySQL support)

pip install psycopg2   # PostgreSQL
pip install pymysql    # MySQL

📂 Project Structure
one-to-many/
│── models.py   # Database models and setup
│── cli.py      # CLI application for managing authors & books
│── database.db # SQLite database (auto-created on first run)
│── README.md   # Project documentation

▶️ Running the Project

Run the CLI app:

python cli.py
