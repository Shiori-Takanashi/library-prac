from pathlib import Path
from typing import List, Callable
from schemas import USER_REQUIRED_KEYS, BOOK_REQUIRED_KEYS
import json
import pytest

ROOT_BOOK_DIR = Path(__file__).parent.parent / "sample" / "books"
ROOT_USER_DIR = Path(__file__).parent.parent / "sample" / "users"
MERGED_BOOK_FILE = Path(__file__).parent.parent / "sample" / "merged_books.json"
MERGED_USER_FILE = Path(__file__).parent.parent / "sample" / "merged_users.json"


def get_json_files(root_dir: Path) -> List[Path]:
    return list(root_dir.glob("**/*.json"))


def get_book_json_files() -> List[Path]:
    return [MERGED_BOOK_FILE]


def get_user_json_files() -> List[Path]:
    return [MERGED_USER_FILE]


def test_json_files_exist() -> None:
    book_files = get_book_json_files()
    user_files = get_user_json_files()
    assert (
        book_files and MERGED_BOOK_FILE.exists()
    ), f"Merged book JSON file not found: {MERGED_BOOK_FILE}"
    assert (
        user_files and MERGED_USER_FILE.exists()
    ), f"Merged user JSON file not found: {MERGED_USER_FILE}"


########################################################################################################

# The data is a list of dictionaries. The consistency of dictionary keys is verified by other tests.
# In the book schema, all dictionaries have the keys: title, author, isbn, total.
# In the user schema, all dictionaries have the keys: id, last_name, first_name, history.
# This function ensures that no duplicate values exist for selected keys only, not all keys.

# Keys to check for duplicates:
# Book schema: title, isbn
# User schema: id

########################################################################################################


@pytest.mark.parametrize(
    "get_files_func, keys_to_check, label",
    [
        (get_book_json_files, ["title", "isbn"], "book"),
        (get_user_json_files, ["id"], "user"),
    ],
)
def test_no_duplicates_in_merged_file(
    get_files_func: Callable[[], list[Path]],
    keys_to_check: list[str],
    label: str,
) -> None:
    """
    Ensure that selected key values do not appear more than once within the merged JSON file.
    """
    seen: dict[str, dict[Any, Path]] = {key: {} for key in keys_to_check}

    for json_file in get_files_func():
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            pytest.fail(
                f"[{label}] Expected list in {json_file}, got {type(data).__name__}"
            )

        for entry in data:
            for key in keys_to_check:
                if key not in entry:
                    pytest.fail(f"[{label}] Missing key '{key}' in {json_file}")
                value = entry[key]
                if value in seen[key]:
                    prev_file = seen[key][value]
                    pytest.fail(
                        f"[{label}] Duplicate '{key}' value '{value}' found in both "
                        f"{prev_file} and {json_file}"
                    )
                seen[key][value] = json_file
