def calculate_per_person(invoice: float, number_of_persons: int, percentage_tip: int = 10) -> float:
    total = invoice + invoice / 100 * percentage_tip
    return total / number_of_persons


print(calculate_per_person(100.0, 5, 0))
print(calculate_per_person(200.0, 4))
print(calculate_per_person(200.0, 4, 50))
