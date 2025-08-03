import allure
import pytest
from pygments.lexers.scripting import all_lua_builtins

from bookstore.models.book import Book
from bookstore.utils.book_utils import (
    discount_price,
    get_books_over_price,
    get_most_expensive_book,
    get_cheapest_book,
    sort_books_by_price,
    get_sorted_highest_to_lowest_book
)

@pytest.fixture
def sample_books():
    return [
        Book("Atomic Habits", "James Clear", 25),
        Book("Deep Work", "Cal Newport", 30),
        Book("The 7 Habits", "Stephen Covey", 20)
    ]

@allure.title("Validate discount_price applies correct discount")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("core","pricing")
@allure.feature("Book Pricing")
@allure.story("Apply discount")
def test_discount_price():
    assert discount_price(100, 0.2) == 80.0
    assert discount_price(50, 0.5) == 25.0

def test_get_books_over_price(sample_books):
    result = get_books_over_price(sample_books, 20)
    assert len(result) == 2
    titles = [b.title for b in result]
    assert "Deep Work" in titles
    assert "Atomic Habits" in titles

def test_get_most_expensive_book(sample_books):
    result = get_most_expensive_book(sample_books)
    assert result.title == "Deep Work"

def test_get_cheapest_book(sample_books):
    result = get_cheapest_book(sample_books)
    assert result.title == "The 7 Habits"

def test_sort_books_by_price_desc(sample_books):
    result = sort_books_by_price(sample_books, descending=True)
    assert result[0].price == 30  # Deep Work
    assert result[-1].price == 20

def test_sort_books_by_price_asc(sample_books):
    result = sort_books_by_price(sample_books, descending=False)
    assert result[0].price == 20  # The 7 Habits
    assert result[-1].price == 30

def test_get_sorted_highest_to_lowest_book(sample_books):
    result = get_sorted_highest_to_lowest_book(sample_books)
    assert [b.price for b in result] == [30, 25, 20]
