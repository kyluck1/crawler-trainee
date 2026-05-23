import os
import sys

# Força o Python a incluir a pasta raiz no caminho de busca
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_path)

# noqa: E402 (Aviso para o linter permitir o import após o ajuste de path)
from main import RATING_MAP, parse_books  # noqa: E402


def test_rating_map_values():
    """Garante que o mapeamento de notas está correto"""
    assert RATING_MAP["One"] == 1
    assert RATING_MAP["Five"] == 5
    assert RATING_MAP.get("Invalid", 0) == 0


def test_parse_books_empty_html():
    """Garante que a função lida bem com HTML sem livros"""
    empty_html = "<html><body><h1>Nenhum livro aqui</h1></body></html>"
    books = parse_books(empty_html)
    assert len(books) == 0
    assert isinstance(books, list)
