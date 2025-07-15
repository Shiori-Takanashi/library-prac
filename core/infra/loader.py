# core/infra/loader.py

import json
from pathlib import Path
from typing import Dict, List, cast

# デフォルトのファイルパス（定数）をインポート
from const.config import ALL_BOOK_JSON, ALL_USER_JSON


def load_book_entities(path: Path = ALL_BOOK_JSON) -> List[Dict[str, str]]:
    """
    JSONファイルから書籍データを読み込んで返す。

    Parameters:
        path: 読み込むJSONファイルのパス（省略時は ALL_BOOK_JSON）

    Returns:
        List[Dict[str, str]]: 書籍情報のリスト（各要素は1冊分の辞書）
    """
    with open(path, "r", encoding="utf-8") as f:
        return cast(List[Dict[str, str]], json.load(f))


def load_user_entities(path: Path = ALL_USER_JSON) -> List[Dict[str, str]]:
    """
    JSONファイルから利用者データを読み込んで返す。

    Parameters:
        path: 読み込むJSONファイルのパス（省略時は ALL_USER_JSON）

    Returns:
        List[Dict[str, str]]: 利用者情報のリスト（各要素は1人分の辞書）
    """
    with open(path, "r", encoding="utf-8") as f:
        return cast(List[Dict[str, str]], json.load(f))
