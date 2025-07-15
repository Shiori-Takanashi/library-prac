"""
JSON を読み込み、図書と利用者を登録して一覧を表示する簡易デモ。
"""

from core.domain.library import Library
from core.infra.factory import make_book_instance, make_user_instance, register_entities
from core.infra.loader import load_book_entities, load_user_entities

lib = Library()

register_entities(load_book_entities(), lib.books, make_book_instance)
register_entities(load_user_entities(), lib.users, make_user_instance)

print("=== 在庫一覧 ===")
for b in lib.list_books().values():
    print(b.stock_status())

print("\n=== ユーザー一覧 ===")
for u in lib.users.values():
    print(u.user_id, u.name)
