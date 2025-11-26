import json
import pathlib

def save_json(path: str, obj):
    p = pathlib.Path(path)
    p.parent.mkdir(exist_ok=True, parents=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
