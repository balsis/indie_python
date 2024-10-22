words = input().lower().split()
print(all(True if "a" in word else False for word in words))