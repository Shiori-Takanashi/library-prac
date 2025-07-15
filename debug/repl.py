"""
対話型 REPL デバッグツール
-------------------------

$ python -m debug.repl

コマンド一覧:
  addbook  "<title>" "<author>" <isbn> <total>
  adduser  <user_id> "<name>"
  lend     <user_id> <isbn>
  return   <user_id> <isbn>
  list     books|users
  history  <user_id>
  help
  quit / exit
"""

import shlex
from cmd import Cmd

from core.domain.book import Book
from core.domain.library import Library
from core.domain.user import User
from utils.init_library import initialize_library


class LibraryREPL(Cmd):
    intro = "図書館 REPL へようこそ。help でコマンド一覧を表示します。"
    prompt = "(library) "

    def __init__(self, lib: Library) -> None:
        super().__init__()
        self.lib = lib

    # ---------- 基本コマンド ---------- #
    def do_addbook(self, arg: str) -> None:
        """addbook "<title>" "<author>" <isbn> <total>"""
        try:
            title, author, isbn, total = shlex.split(arg)
            self.lib.register_book(Book(title, author, isbn, int(total)))
            print(f"登録完了: {title} ({isbn})")
        except ValueError:
            print('使い方: addbook "<title>" "<author>" <isbn> <total>')

    def do_adduser(self, arg: str) -> None:
        """adduser <user_id> "<name>\" """
        try:
            user_id, name = shlex.split(arg)
            self.lib.register_user(User(user_id, name, []))
            print(f"利用者登録完了: {name} ({user_id})")
        except ValueError:
            print('使い方: adduser <user_id> "<name>"')

    def do_lend(self, arg: str) -> None:
        """lend <user_id> <isbn>"""
        try:
            user_id, isbn = arg.split()
            self.lib.lend_book(user_id, isbn)
            print(f"貸出完了: {isbn} → {user_id}")
        except Exception as e:
            print(e)

    def do_return(self, arg: str) -> None:
        """return <user_id> <isbn>"""
        try:
            user_id, isbn = arg.split()
            self.lib.return_book(user_id, isbn)
            print(f"返却完了: {isbn} ← {user_id}")
        except Exception as e:
            print(e)

    def do_list(self, arg: str) -> None:
        """list books|users"""
        if arg.strip() == "books":
            for b in self.lib.list_books().values():
                print(b.stock_status())
        elif arg.strip() == "users":
            for u in self.lib.users.values():
                print(f"{u.user_id}: {u.name}")
        else:
            print("使い方: list books もしくは list users")

    def do_history(self, arg: str) -> None:
        """history <user_id>"""
        user_id = arg.strip()
        try:
            for line in self.lib.get_user_history(user_id):
                print(line)
        except Exception as e:
            print(e)

    # ---------- 補助 ---------- #
    def do_help(self, arg: str) -> None:
        commands = {
            "addbook": 'addbook "<title>" "<author>" <isbn> <total>',
            "adduser": 'adduser <user_id> "<name>"',
            "lend": "lend <user_id> <isbn>",
            "return": "return <user_id> <isbn>",
            "list": "list books | users",
            "history": "history <user_id>",
            "quit": "quit（または exit でも可）",
        }
        print("📚 利用可能なコマンド一覧：")
        for cmd, usage in commands.items():
            print(f"  {cmd:<8} : {usage}")

    def do_quit(self, _: str) -> bool:
        """quit"""
        return True

    do_exit = do_quit  # alias


if __name__ == "__main__":
    lib = initialize_library()
    LibraryREPL(lib).cmdloop()
