from typing import List
from bookstore.models.book import Book

def discount_price(price: float, percentage: float) -> float:
    """Apply a discount to a raw price (not a Book object)."""
    return round(price * (1 - percentage), 2)

def get_books_over_price(books: List[Book], min_price: float) -> List[Book]:
    """Return books priced above the given threshold."""
    return [book for book in books if book.price > min_price]

def get_most_expensive_book(books: List[Book]) -> Book:
    """Return the single most expensive book."""
    if not books:
        raise ValueError("Book list is empty")
    return max(books, key=lambda b: b.price)

def sort_books_by_price(books: List[Book], descending: bool = True) -> List[Book]:
    """Return a list of books sorted by price."""
    return sorted(books, key=lambda b: b.price, reverse=descending)

def get_cheapest_book(books: List[Book]) -> Book:
    """Return the single cheapest book."""
    if not books:
        raise ValueError("Book list is empty")
    return min(books, key=lambda b: b.price)

def get_sorted_highest_to_lowest_book(books: List[Book]) -> List[Book]:
    """Return a list of books sorted by price from highest to lowest."""
    if not books:
        raise ValueError("Book list is empty")
    return sorted(books, key=lambda b: b.price, reverse=True)