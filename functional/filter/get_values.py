def get_values(nums: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(lambda x: x * 3, filter(lambda x: x % 3 == 0, nums)))


nums = (2, 12, 5, 9, 3, 16, 7, 13, 21, 1, 15, 4, 20, 11)
print(get_values(nums))