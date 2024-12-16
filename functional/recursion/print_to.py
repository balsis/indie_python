def print_to(n):
    if n > 0:
        print_to(n-1)
        print(n)

print_to(5)

# #1
# 2
# 3
# 4
# 5
lst = [1, 2, 1, 3, 1, 2, 1]
print(sum(lst))