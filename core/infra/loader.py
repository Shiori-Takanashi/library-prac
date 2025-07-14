import json
from pathlib import Path
from typing import Dict, List, cast


def load_entities(path: Path) -> List[Dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        return cast(List[Dict[str, str]], json.load(f))
