lst = []
for i in range(int(input())):
    lst.append(int(input()))

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

result = gcd(lst[0], lst[1])
for i in lst[2:]:
    result = gcd(result, i)

print(result)