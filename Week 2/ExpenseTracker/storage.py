import json
from typing import Dict

FILE_PATH = "expenses.json"

def load_expenses() -> Dict[str, float]:
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {k: float(v) for k, v in data.items()}
    except FileNotFoundError:
        return {}  # start empty
    except (json.JSONDecodeError, ValueError):
        # corrupted file or bad values
        print("Warning: could not parse expenses.json. Starting fresh.")
        return {}

def save_expenses(expenses: Dict[str, float]) -> None:
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)
