"""
📦 Gitリポジトリ情報の取得スクリプト（モジュール実行専用・非CLI）

- リポジトリのブランチ・リモート・コミット・ステータスなどを収集
- 詳細な構成情報（タグ、hooks、設定、変更概要）も含む
- 出力は JSON ファイルとして保存（定数でパス指定）
- CLI引数やprint出力は一切なし。CIやバッチ用途を想定

使用例:
$ python -m tools.repo_info_minimal
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path

# ==== 設定定数 ====

REPO_PATH = Path.cwd()  # 実行時の作業ディレクトリ（プロジェクトルートでの -m 実行前提）
OUTPUT_PATH = REPO_PATH / "out" / "current_repo_info.json"
TEMPLATE_PATH = None  # 例: Path("tools/repo_base/template_repo_info.json") にテンプレを置く想定（未使用）


# ==== Gitユーティリティ関数 ====


def git(cmd: list[str]) -> str | None:
    """gitコマンドを実行し、標準出力を返す（失敗時はNone）"""
    try:
        return subprocess.run(
            ["git"] + cmd,
            cwd=REPO_PATH,
            text=True,
            capture_output=True,
            check=True,
            encoding="utf-8",  # ← 追加
            errors="replace",  # ← 追加推奨（不正文字も落とさず通す）
        ).stdout.strip()
    except subprocess.CalledProcessError:
        return None


def parse_status(output: str | None) -> dict:
    """git status --porcelain の出力を分類（ステージ済・変更済・未追跡）"""
    if not output:
        return {"staged": [], "modified": [], "untracked": [], "is_clean": True}
    staged, modified, untracked = [], [], []
    for line in output.splitlines():
        code, file = line[:2], line[3:]
        if code[0] in "AMDRC":
            staged.append(file)
        if code[1] in "MD":
            modified.append(file)
        if code == "??":
            untracked.append(file)
    return {
        "staged": staged,
        "modified": modified,
        "untracked": untracked,
        "is_clean": not (staged or modified or untracked),
    }


def parse_lines(output: str | None, skip_head: bool = False) -> list[str]:
    """行分割してリスト化（必要なら HEAD 参照を除外）"""
    if not output:
        return []
    lines = output.splitlines()
    if skip_head:
        lines = [l for l in lines if not l.startswith("origin/HEAD")]
    return [l.strip().lstrip("* ").strip() for l in lines]


def parse_recent_commits(output: str | None) -> list[dict]:
    """最新のコミット履歴（ハッシュ・著者・日時・メッセージ）を辞書リストで返す"""
    if not output:
        return []
    commits = []
    for line in output.splitlines():
        parts = line.strip().split(" ", 3)
        if len(parts) == 4:
            commits.append(
                {
                    "hash": parts[0],
                    "author": parts[1],
                    "date": parts[2],
                    "message": parts[3],
                }
            )
    return commits


def parse_hooks(hook_dir: Path) -> list[str]:
    """.git/hooks 内の有効な（.sample以外の）フックを抽出"""
    if not hook_dir.exists():
        return []
    return [
        f.name
        for f in hook_dir.iterdir()
        if f.is_file() and not f.name.endswith(".sample")
    ]


# ==== リポジトリ情報の収集 ====


def get_repo_info() -> dict:
    """包括的なリポジトリ情報を構造化して返す"""
    return {
        "timestamp": datetime.now().isoformat(),
        "repository_path": str(REPO_PATH),
        "current_branch": git(["branch", "--show-current"]),
        "remote_url": git(["remote", "get-url", "origin"]),
        "latest_commit": {
            "hash": git(["rev-parse", "HEAD"]),
            "message": git(["log", "-1", "--pretty=format:%s"]),
            "author": git(["log", "-1", "--pretty=format:%an"]),
            "date": git(["log", "-1", "--pretty=format:%ci"]),
        },
        "recent_commits": parse_recent_commits(
            git(["log", "-10", "--pretty=format:%h %an %ad %s", "--date=iso"])
        ),
        "status": parse_status(git(["status", "--porcelain"])),
        "diff_summary": git(["diff", "--stat"]),
        "tracked_files": parse_lines(git(["ls-files"])),
        "local_branches": parse_lines(git(["branch"])),
        "remote_branches": parse_lines(git(["branch", "-r"]), skip_head=True),
        "tags": parse_lines(git(["tag"])),
        "hooks_enabled": parse_hooks(REPO_PATH / ".git" / "hooks"),
        "git_config": parse_lines(git(["config", "--list"])),
    }


# ==== 保存処理 ====


def save_repo_info() -> Path:
    """リポジトリ情報を JSON ファイルとして保存し、そのパスを返す"""
    info = get_repo_info()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2, ensure_ascii=False)
    return OUTPUT_PATH


# ==== 実行エントリポイント ====

if __name__ == "__main__":
    save_repo_info()
