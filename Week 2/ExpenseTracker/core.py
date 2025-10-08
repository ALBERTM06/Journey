from typing import Dict

def add_expense(expenses: Dict[str, float], item: str, amount: float) -> None:
    if amount < 0:
        raise ValueError("Amount must be non-negative.")
    expenses[item] = expenses.get(item, 0.0) + amount  # accumulate by item

def total_expenses(expenses: Dict[str, float]) -> float:
    return sum(expenses.values())

def list_expenses(expenses: Dict[str, float]) -> str:
    if not expenses:
        return "No expenses yet."
    lines = [f"- {k}: {v:.2f}" for k, v in expenses.items()]
    return "\n".join(lines)
