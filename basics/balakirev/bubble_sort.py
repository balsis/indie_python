lst = list  (
    map(int, input().split())
)

for index in range(len(lst)):
    for value in range(len(lst) - index - 1):
        if lst[value] > lst[value+1]:
            lst[value], lst[value+1] = lst[value+1], lst[value]
    #print(lst)

print(*lst)