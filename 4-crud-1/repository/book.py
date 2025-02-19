class BookRepository:
    def __init__(self):
        self.books = [
            {'id': 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "total_pages": 310, "genre": "Fantasy"},
            {'id': 2, "title": "1984", "author": "George Orwell", "year": 1949, "total_pages": 328, "genre": "Dystopian"},
            {'id': 3, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "total_pages": 279, "genre": "Romance"},
            {'id': 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "total_pages": 281, "genre": "Fiction"},
            {'id': 5, "title": "Moby-Dick", "author": "Herman Melville", "year": 1851, "total_pages": 635, "genre": "Adventure"},
            {'id': 6, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "total_pages": 180, "genre": "Classic"},
            {'id': 7, "title": "War and Peace", "author": "Leo Tolstoy", "year": 1869, "total_pages": 1225, "genre": "Historical"},
            {'id': 8, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866, "total_pages": 671, "genre": "Psychological Fiction"},
            {'id': 9, "title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "total_pages": 311, "genre": "Dystopian"},
            {'id': 10, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "total_pages": 277, "genre": "Coming-of-age"},
            {'id': 11, "title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez", "year": 1967, "total_pages": 417, "genre": "Magical Realism"},
            {'id': 12, "title": "Les Misérables", "author": "Victor Hugo", "year": 1862, "total_pages": 1463, "genre": "Historical"},
            {'id': 13, "title": "Anna Karenina", "author": "Leo Tolstoy", "year": 1877, "total_pages": 864, "genre": "Romance"},
            {'id': 14, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "year": 1880, "total_pages": 796, "genre": "Philosophical"},
            {'id': 15, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "year": 1890, "total_pages": 254, "genre": "Gothic Fiction"},
            {'id': 16, "title": "Wuthering Heights", "author": "Emily Brontë", "year": 1847, "total_pages": 416, "genre": "Gothic Fiction"},
            {'id': 17, "title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953, "total_pages": 249, "genre": "Dystopian"},
            {'id': 18, "title": "Dracula", "author": "Bram Stoker", "year": 1897, "total_pages": 418, "genre": "Horror"},
            {'id': 19, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954, "total_pages": 1178, "genre": "Fantasy"},
            {'id': 20, "title": "The Stranger", "author": "Albert Camus", "year": 1942, "total_pages": 123, "genre": "Philosophical"},
            {'id': 21, "title": "Don Quixote", "author": "Miguel de Cervantes", "year": 1605, "total_pages": 1072, "genre": "Adventure"},
            {'id': 22, "title": "The Divine Comedy", "author": "Dante Alighieri", "year": 1320, "total_pages": 798, "genre": "Epic Poetry"},
            {'id': 23, "title": "The Odyssey", "author": "Homer", "year": -800, "total_pages": 541, "genre": "Epic Poetry"},
            {'id': 24, "title": "Madame Bovary", "author": "Gustave Flaubert", "year": 1856, "total_pages": 328, "genre": "Realism"},
            {'id': 25, "title": "Ulysses", "author": "James Joyce", "year": 1922, "total_pages": 730, "genre": "Modernist Fiction"},
            {'id': 26, "title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "year": 1844, "total_pages": 1276, "genre": "Adventure"},
            {'id': 27, "title": "The Iliad", "author": "Homer", "year": -750, "total_pages": 683, "genre": "Epic Poetry"},
            {'id': 28, "title": "Frankenstein", "author": "Mary Shelley", "year": 1818, "total_pages": 280, "genre": "Gothic Fiction"},
            {'id': 29, "title": "The Metamorphosis", "author": "Franz Kafka", "year": 1915, "total_pages": 201, "genre": "Absurdist Fiction"},
            {'id': 30, "title": "The Old Man and the Sea", "author": "Ernest Hemingway", "year": 1952, "total_pages": 127, "genre": "Classic"},
        ]

    def get_all(self, start: int, end: int 
    ):
        if start < 0 or start >= len(self.books):
            return []
        elif end < 0:
            return []
        return self.books[start:end]
    
    def get_len(self):
        return len(self.books)
    
    def get_one(self, id:int):
        book = next((book for book in self.books if book["id"] == id), [])
        return book
    
    def save(self, book):
        if "id" not in book or not book["id"]:
            book["id"] = self.get_new_id()
        self.books.append(book)
        return book
    
    def get_new_id(self):
        return len(self.books)+1