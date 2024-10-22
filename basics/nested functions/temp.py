def color() -> None:
    g = 'green'

    def grey() -> None:
        nonlocal g
        g = 'grey'
        print(g)

    grey()
    print(g)


color()