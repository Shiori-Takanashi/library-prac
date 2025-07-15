import pytest

from core.domain.user import User


def test_borrow_and_return_history() -> None:
    user = User("u1", "山田 太郎", history=[])

    # 初回貸出
    user.borrow_book("isbn1")
    assert "isbn1" in user.borrowed_books
    assert user.history[-1] == "借用: isbn1"

    # 二重借用は ValueError を期待（例外が発生することを確認）
    with pytest.raises(ValueError):
        user.borrow_book("isbn1")

    # 返却
    user.return_book("isbn1")
    assert "isbn1" not in user.borrowed_books
    assert user.history[-1] == "返却: isbn1"

    # 借りていない本を返そうとすると ValueError を期待
    with pytest.raises(ValueError):
        user.return_book("isbn1")
