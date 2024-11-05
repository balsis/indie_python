def print_scores(name, *args):
    print(f'Student name: {name}')
    for i in sorted(args):
        print(i)

print_scores("Jud", 100, 95, 88, 92, 99)
