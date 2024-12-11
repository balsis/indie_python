weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = ((i + 1, weekdays[(5 + i) % 7]) for i in range(365))

for i in range(77):
    print(next(days))