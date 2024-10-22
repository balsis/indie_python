a = int(input())
b = list(map(int, input().split()))
def rec(a):
    if a > 0:
        rec(a - 1)
        print(b[-a], end=" ")


rec(a)