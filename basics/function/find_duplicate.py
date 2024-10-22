def find_duplicate(lst):
    main = []
    count = 0
    for i in lst:
        if i not in main and lst.count(i) > 1:
            main.append(i)
    return main

print(find_duplicate([1, 2, 3, 4]))
