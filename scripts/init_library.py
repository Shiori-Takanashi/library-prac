# scripts/init_library.py

"""
JSON を読み込み、図書と利用者を登録。
"""

from core.domain.library import Library
from core.infra.factory import make_book_instance, make_user_instance, register_entities
from core.infra.loader import load_book_entities, load_user_entities


def initialize_library() -> Library:
    """JSONから図書と利用者を読み込んで登録済みのLibraryを返す"""
    lib = Library()
    register_entities(load_book_entities(), lib.books, make_book_instance)
    register_entities(load_user_entities(), lib.users, make_user_instance)
    return lib
