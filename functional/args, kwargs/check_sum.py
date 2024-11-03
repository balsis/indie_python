def check_sum(*args):
    print("not enough" if sum(args) < 50 else "verification passed")


check_sum(8, 11)
check_sum(10, 10, 10, 10, 9)
check_sum(20, 20, 10)
