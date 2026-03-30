def find_smallest(arr: list):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


aa = [3, 33, 3, 44, 4, 13]


def selection_sort(arr: list):
    new = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new.append(arr.pop(smallest))
    return new


print(selection_sort(arr=aa))