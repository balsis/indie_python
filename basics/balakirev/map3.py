s = input().split()

new = map(lambda x: x if len(x) > 5 else "-", s)



print(" ".join(new))