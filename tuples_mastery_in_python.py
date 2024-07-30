from helper import d


def format_itineraries(itineraries):    
    for i, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        print(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")

# Example usage
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
format_itineraries(itineraries)

d()

def add_book(library, book):
    if book in library:
        print("This book is already in the library.")
    else:
        library.append(book)
        print("Book added successfully.")


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

new_book = ("To Kill a Mockingbird", "Harper Lee")
add_book(library, new_book)  # This should add the book

duplicate_book = ("1984", "George Orwell")
add_book(library, duplicate_book)  # This should indicate the book is already in the library

print(library)
