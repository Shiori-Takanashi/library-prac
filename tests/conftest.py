# tests/conftest.py

import pytest

from core.domain.book import Book
from core.domain.user import User


@pytest.fixture
def sample_book() -> Book:
    return Book(title="吾輩は猫である", author="夏目漱石", isbn="123", total=3)


@pytest.fixture
def sample_user() -> User:
    return User(user_id="u1", name="山田 太郎", history=[])
