from typing import Dict, List


def transform_info(info: List[Dict[str, str]]) -> List[List[str]]:
    if not info:
        return []
    keys = list(info[0].keys())
    return [[entry[key] for key in keys] for entry in info]


def show_info(info: List[Dict[str, str]]) -> None:
    for line in transform_info(info):
        print(", ".join(str(x) for x in line))
