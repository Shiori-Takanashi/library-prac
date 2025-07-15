import subprocess
from pathlib import Path
from typing import List, Tuple


def get_installed_extensions() -> List[Tuple[str, str]]:
    """code --list-extensions --show-versions の出力を (id, version) のリストに変換"""
    try:
        result = subprocess.run(
            ["code", "--list-extensions", "--show-versions"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            encoding="utf-8",
        )
        lines = result.stdout.strip().splitlines()
        exts: List[Tuple[str, str]] = []
        for line in lines:
            if "@" in line:
                ext_id, version = line.strip().split("@", 1)
                exts.append((ext_id, version))
        return exts
    except FileNotFoundError:
        print("❌ 'code' コマンドが使えません。VS Code の PATH を確認してください。")
        return []
    except subprocess.CalledProcessError as e:
        print(f"❌ コマンド実行エラー: {e}")
        return []


def export_to_markdown_list(exts: List[Tuple[str, str]], output_path: Path) -> None:
    """拡張機能のリストを箇条書きのMarkdown形式で保存"""
    lines: List[str] = ["# インストール済み VS Code 拡張機能一覧", ""]
    lines.extend([f"- {ext_id} @ {version}" for ext_id, version in exts])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ 拡張機能一覧を出力しました → {output_path}")


def main() -> None:
    output_path = Path(__file__).resolve().parents[1] / "docs" / "vscode_extensions.md"
    extensions = get_installed_extensions()
    if extensions:
        export_to_markdown_list(extensions, output_path)


if __name__ == "__main__":
    main()
