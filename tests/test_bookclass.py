import pytest
from core.book import Book


def test_check_bookobj_01():
    """Bookオブジェクト生成と属性初期化（None）の確認"""
    book = Book()
    assert isinstance(book, Book)
    assert book.title is None
    assert book.author is None
    assert book.isbn is None
    assert book.total is None


def test_check_bookobj_02():
    """add_bookで1回だけ登録したときの属性反映"""
    book = Book()
    book.add_book("ノルウェイの森", "村上春樹", "novel-murakami", 3)
    assert book.title == "ノルウェイの森"
    assert book.author == "村上春樹"
    assert book.isbn == "novel-murakami"
    assert book.total == 3


def test_check_bookobj_03():
    """同じ本に対してadd_bookを2回呼び、在庫が加算されることの確認"""
    book = Book()
    book.add_book("ノルウェイの森", "村上春樹", "novel-murakami", 3)
    book.add_book("ノルウェイの森", "村上春樹", "novel-murakami", 2)
    assert book.total == 5


def test_check_bookobj_04():
    """異なる本として別インスタンスで登録しても干渉しないことの確認"""
    b1 = Book()
    b2 = Book()
    b1.add_book("仮面の告白", "三島由紀夫", "novel-mishima", 2)
    b2.add_book("人間失格", "太宰治", "novel-dazai", 3)
    assert b1.title != b2.title
    assert b1.total == 2
    assert b2.total == 3


def test_check_bookobj_05():
    """同じISBNで違うタイトルを渡した場合に上書きされることの確認"""
    book = Book()
    book.add_book("ノルウェイの森", "村上春樹", "novel-murakami", 1)
    book.add_book("海辺のカフカ", "村上春樹", "novel-murakami", 1)
    assert book.title == "海辺のカフカ"
    assert book.total == 2


def test_check_bookobj_06():
    """合算処理でNoneの初期値がint型に変わることの確認"""
    book = Book()
    book.add_book("火花", "又吉直樹", "novel-matayoshi", 1)
    assert isinstance(book.total, int)


def test_check_bookobj_07():
    """属性の型検証"""
    book = Book()
    book.add_book("蜜蜂と遠雷", "恩田陸", "novel-onda", 4)
    assert isinstance(book.title, str)
    assert isinstance(book.author, str)
    assert isinstance(book.isbn, str)
    assert isinstance(book.total, int)


def test_check_bookobj_08():
    """total が負数やゼロを受け入れるか（設計の曖昧さを確認）"""
    book = Book()
    book.add_book("銀河鉄道の夜", "宮沢賢治", "novel-miyazawa", -1)
    assert book.total == -1  # 実装上は可能だが、要検討事項


def test_check_bookobj_09():
    """登録直後の状態をタプルで比較して検証"""
    book = Book()
    book.add_book("吾輩は猫である", "夏目漱石", "novel-natsume", 5)
    actual = (book.title, book.author, book.isbn, book.total)
    expected = ("吾輩は猫である", "夏目漱石", "novel-natsume", 5)
    assert actual == expected
