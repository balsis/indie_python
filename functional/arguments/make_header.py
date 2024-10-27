def make_header(text: str, level: int)-> str:
    return f'<h{level}>{text}</h{level}>'

print(make_header('Нет', 1))
print(make_header('Bella Ciao', 4))
print(make_header(text='Go little rock star', level=6))
print(make_header(level=2, text='Девальвации не будет. Твердо и четко'))
