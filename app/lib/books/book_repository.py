from .book import Book

class BookRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        # self._connection.seed("seeds/books.sql")
        
        rows = self._connection.execute('SELECT * from books')
        books = []

        for row in rows:
            item = Book(row["id"], row["title"], row["author"])
            books.append(item)

        return books
    
    def create(self, new_book):
        title = new_book.get("title")
        author = new_book.get("author")
        # print(title, author)

        # do not make the mistake of using quotes again as it will leave 
        # the app open to sql injection attacks ):
        self._connection.execute(f"INSERT INTO books (title, author) VALUES (%s, %s)", [title, author])

        print("book created successfully")

        return None
    
    def find(self, id):
        # get only first item
        # there should only be one item since it gets by id
        # and all id's should be unique
        query_result = self._connection.execute("SELECT * FROM books WHERE id = %s", [id])[0]

        # print(f">>> QUERY RESULT: {query_result}")

        # unpack vals with kwargs
        book = Book(**query_result)
        
        return book