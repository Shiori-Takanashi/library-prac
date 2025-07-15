# Repository Information Tool

このツールは、Gitリポジトリの情報を取得・保存するためのPythonモジュールです。

## ファイル構成

- `repo_info.py`: メインのリポジトリ情報取得モジュール
- `demo_repo_info.py`: 使用例とデモンストレーション
- `README.md`: このファイル

## 機能

### RepositoryInfoクラス

リポジトリの以下の情報を取得できます：

- 現在のブランチ名
- リモートURL
- 最新コミット情報（ハッシュ、メッセージ、作者、日時）
- リポジトリステータス（ステージング、変更、未追跡ファイル）
- ローカルブランチ一覧
- リモートブランチ一覧
- 総合的なリポジトリ情報

## 使用方法

### プログラムでの使用

```python
from repo_info import RepositoryInfo

# 現在のディレクトリのリポジトリ情報を取得
repo = RepositoryInfo()

# 現在のブランチを取得
current_branch = repo.get_current_branch()
print(f"Current branch: {current_branch}")

# 全ての情報を取得
info = repo.get_repo_info()

# JSON ファイルに保存
output_file = repo.save_repo_info()
print(f"Information saved to: {output_file}")
```

### コマンドラインでの使用

```bash
# リポジトリ情報をコンソールに出力
python repo_info.py --print

# リポジトリ情報をファイルに保存
python repo_info.py --output my_repo_info.json

# 特定のパスのリポジトリ情報を取得
python repo_info.py --path /path/to/repo --print
```

### デモの実行

```bash
# デモスクリプトを実行
python demo_repo_info.py
```

## 出力例

```json
{
  "timestamp": "2025-07-15T06:35:17.123456",
  "repository_path": "/path/to/repo",
  "current_branch": "main",
  "remote_url": "https://github.com/user/repo.git",
  "latest_commit": {
    "hash": "abc123...",
    "message": "Add new feature",
    "author": "Developer Name",
    "date": "2025-07-15 06:30:00 +0900"
  },
  "status": {
    "staged": [],
    "modified": ["file1.py"],
    "untracked": ["new_file.py"],
    "is_clean": false
  },
  "local_branches": ["main", "feature-branch"],
  "remote_branches": ["origin/main", "origin/develop"]
}
```

## 必要な依存関係

- Python 3.7+
- Gitがシステムにインストールされている必要があります

## 注意事項

- このツールはGitリポジトリ内で実行する必要があります
- Gitコマンドが利用可能である必要があります
- エラーが発生した場合、該当する情報はNoneまたは空のリストが返されます
