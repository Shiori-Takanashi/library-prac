# tools/prepare_sample_data.py
import json
from pathlib import Path


def merge_and_dedup(dir_path: Path, key_fields: list[str]) -> list[dict]:
    files = sorted(dir_path.glob("*.json"))
    unique_entries = {}
    for file in files:
        with file.open("r", encoding="utf-8") as f:
            data = json.load(f)
        for entry in data:
            key = tuple(entry.get(k) for k in key_fields)
            if key not in unique_entries:
                unique_entries[key] = entry
    return list(unique_entries.values())


def save_merged(output_path: Path, data: list[dict]) -> None:
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    books = merge_and_dedup(Path("data/books"), ["isbn"])
    save_merged(Path("data/all_books.json"), books)

    users = merge_and_dedup(Path("data/users"), ["id"])
    save_merged(Path("data/all_users.json"), users)
