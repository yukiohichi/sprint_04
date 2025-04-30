import pytest

from main import BooksCollector

@pytest.fixture(scope='function')
def books_collector():
    collector = BooksCollector()
    books = {
        'Путешествие в Элевсин': 'Ужасы',
        'Чебурашка': 'Мультфильмы',
        'Большие надежды': 'Комедии'
    }
    for name, genre in books.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    collector.add_book_in_favorites('Большие надежды')
    return collector
