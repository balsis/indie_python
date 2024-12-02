lst = list(map(int, input().split()))
check = all([True if (int(lst[i]) > int(lst[i + 1])) else False for i in range (len(lst)-1)])
print(check)


