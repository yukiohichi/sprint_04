import pytest


from main import BooksCollector


class TestBooksCollector:

#тесты на добавление новых книг
    @pytest.mark.parametrize(
        'list_book, result',
        [
            ('Мать тьма', +1),
            ('Путешествие в Элевсин', 0),
            ('', 0),
            ('Так говорил заратустра или не говорил кто его знает', 0)
        ],
        ids=[
            'should add new book',
            'should not add duplicate book',
            'should reject empty name',
            'should reject long name'
        ]
    )
    def test_add_new_book(self, list_book, result, books_collector):
        initial_count = len(books_collector.get_books_genre())
        books_collector.add_new_book(list_book)
        final_count = len(books_collector.get_books_genre())
        assert final_count - initial_count == result

#тесты на установление жанра книге
    @pytest.mark.parametrize(
        'book_name, genre, expected_genre',
        [
            ('Путешествие в Элевсин', 'Ужасы', 'Ужасы'),
            ('Тьма', 'Ужасы', None),
            ('Путешествие в Элевсин', 'Приколы', 'Ужасы'),
            ('Тьма', 'Приколы', None),
        ],
        ids=[
            'correct book correct genre',
            'unknown book correct genre',
            'correct book unknown genre',
            'unknown book unknown genre',

        ]
    )
    def test_set_book_genre(self, book_name, genre, expected_genre, books_collector):
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == expected_genre

#тест на получение жанра книги по имени
    def test_get_book_genre_success(self, books_collector):
        book_name = 'Путешествие в Элевсин'
        expected_genre = 'Ужасы'
        assert books_collector.get_book_genre(book_name) == expected_genre

#тесты на вывод книг с определенным жанром
    @pytest.mark.parametrize(
        'genre, expected_books',
        [
        ('Ужасы', ['Путешествие в Элевсин']),
        ('Приколы', []),  # Несуществующий жанр
        ('', [])  # Пустой жанр
        ],
        ids=[
            'correct book correct genre',
            'unknown genre',
            'zero genre'
        ]
        )
    def test_get_books_with_different_genres(self, genre, expected_books, books_collector):
        result = books_collector.get_books_with_specific_genre(genre)
        assert result == expected_books

#проверка, что выводится три книги из словаря
    def test_get_books_genre_in_three(self, books_collector):
        assert len(books_collector.get_books_genre()) == 3

#тест на вывод книг, подходящих детям
    def test_get_books_for_children_success(self, books_collector):
        assert books_collector.get_books_for_children() == ['Чебурашка', 'Большие надежды']

#тесты на добавление книг в Избранное
    @pytest.mark.parametrize(
        'name_book, result',
        [
        ('Путешествие в Элевсин', 2),
        ('Большие надежды', 1),
        ('Тьма', 1)
        ],
        ids=[
            'correct book in favorites',
            'incorrect book not in favorites',
            'unknown book not in favorites'
        ]
    )
    def test_add_book_in_favorites(self, name_book, result, books_collector):
        books_collector.add_book_in_favorites(name_book)
        assert len(books_collector.get_list_of_favorites_books()) == result

#тест на корректное удаление книги из избранного
    @pytest.mark.parametrize(
        'book, result',
        [
            ('Большие надежды', 0),
            ('Тьма', 1)
        ],
        ids=[
            'correct delete book',
            'incorrect book not in delete',
        ]
    )
    def test_delete_book_from_favorites_correct_delete(self, book, result, books_collector):
        books_collector.delete_book_from_favorites(book)
        assert len(books_collector.get_list_of_favorites_books()) == result

#тест на получение списка избранных книг
    def test_get_list_of_favorites_books_success(self, books_collector):
        assert 'Большие надежды' in books_collector.get_list_of_favorites_books()
