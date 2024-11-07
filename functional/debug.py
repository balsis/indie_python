def get_total(price: float, qty: int = 1) -> None:
    total: float = price * qty
    print(f'Cost ${total:.2f}')


print(get_total.__annotations__)
