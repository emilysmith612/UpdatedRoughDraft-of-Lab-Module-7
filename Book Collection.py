# Constants
TITLE = "title"
AUTHOR = "author"
GENRE = "genre"
ISBN = "isbn"
TAGS = "tags"

# Genres
FANTASY = "Fantasy"
SCIFI = "Sci-Fi"
MYSTERY = "Mystery"

# Tags
DRAMA = "drama"
THRILLER = "thriller"
SUSPENSE = "suspense"
PSYCHOLOGICAL = "psychological"
LONG = "long"
EPIC = "epic"
TRAUMA = "trauma"

# Functions

def get_book(collection, isbn):
    """
    Returns a tuple (title, author) if a book with the given ISBN is found.
    Otherwise, returns an empty tuple.
    """
    for book in collection:
        if book[ISBN] == isbn:
            return (book[TITLE], book[AUTHOR])
    return ()

def add_book(collection, title, author, genre, isbn, tags):
    """
    Adds a book to the collection if the ISBN doesn't already exist.
    Returns a new collection list.
    """
    if get_book(collection, isbn):  # Check for ISBN conflict
        print(f"ISBN '{isbn}' already exists. Book not added.")
        return collection

    new_book = {
        TITLE: title,
        AUTHOR: author,
        GENRE: genre,
        ISBN: isbn,
        TAGS: set(tags)  # Convert tuple to set
    }

    new_collection = collection.copy()
    new_collection.append(new_book)
    return new_collection

def books_with_tags(collection, tags):
    """
    Returns a list of books that have all the specified tags.
    """
    tag_set = set(tags)
    return [book for book in collection if tag_set.issubset(book[TAGS])]

def books_by_genre(collection, genre):
    """
    Returns a list of books that match a given genre.
    """
    return [book for book in collection if book[GENRE].lower() == genre.lower()]

def list_authors(collection):
    """
    Returns a set of unique authors from the collection.
    """
    return set(book[AUTHOR] for book in collection)

# Tests
def run_tests():
    books = []

    # Test 1: Add the first book
    books = add_book(books, "The Way of Kings", "Brandon Sanderson", FANTASY, "9780765365279",
                     (EPIC, TRAUMA, LONG))
    assert len(books) == 1, "Book should be added"

    # Test 2: Attempt to add a duplicate ISBN
    books = add_book(books, "Duplicate Book", "Someone Else", FANTASY, "9780765365279", (DRAMA,))
    assert len(books) == 1, "Duplicate ISBN should not be added"

    # Test 3: Add a second unique book
    books = add_book(books, "Dark Matter", "Blake Crouch", SCIFI, "1101904224",
                     (THRILLER, SUSPENSE, PSYCHOLOGICAL))
    assert len(books) == 2, "Second book should be added"

    # Test 4: Find book by ISBN
    assert get_book(books, "9780765365279") == ("The Way of Kings", "Brandon Sanderson"), "get_book failed"
    assert get_book(books, "0000000000") == (), "get_book should return empty for unknown ISBN"

    # Test 5: Find books with specific tags
    result = books_with_tags(books, (EPIC, TRAUMA))
    assert len(result) == 1 and result[0][TITLE] == "The Way of Kings", "books_with_tags failed"

    # Test 6: Search books by genre
    result = books_by_genre(books, FANTASY)
    assert len(result) == 1 and result[0][TITLE] == "The Way of Kings", "books_by_genre failed"

    # Test 7: List unique authors
    authors = list_authors(books)
    assert "Brandon Sanderson" in authors and "Blake Crouch" in authors, "list_authors failed"

    print("All tests passed!")

run_tests()
