from pathlib import Path
from typing import List

IGNORE_DIRS = [".venv", ".git", ".pytest_cache", "__pycache__", ".mypy_cache"]


def get_all_children(root_dir: Path) -> List[Path]:
    """
    Recursively get all child files and directories, ignoring specified folders.
    """
    if not root_dir.exists():
        raise ValueError(f"{root_dir} does not exist.")

    if root_dir.is_file():
        raise ValueError(f"{root_dir} is a file, not a directory.")

    children: List[Path] = []

    for child in root_dir.iterdir():
        if any(ignored in child.parts for ignored in IGNORE_DIRS):
            continue

        if child.is_dir():
            children.extend(get_all_children(child))  # ← ネストしないようにextend
        else:
            children.append(child)

    return children


def write_all_children(outpath: Path, children: List) -> None:
    with open(outpath, "w", encoding="utf-8") as f:
        f.write("# This file is named tree.txt.\n# It was made by tree.py-script.\n\n")
        f.write("# Files #\n")
        for item in children:
            f.write(f"{item}\n")
        f.write("\n# ignore dirs #\n")
        f.write("\n".join(IGNORE_DIRS))


if __name__ == "__main__":
    rootpath = Path(r"C:\Users\ns69a\winprojects\library-lesson")
    outdir = rootpath / "out"
    outdir.mkdir(exist_ok=True)
    outfile = outdir / "tree.txt"

    children = get_all_children(rootpath)
    write_all_children(outfile, children)
