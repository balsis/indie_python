def calculate_high_low_avg(*args, log_to_console=False):
    avg = (max(args) + min(args)) / 2
    return f"high={max(args)}, low={min(args)}, avg={avg}\n{avg}" if log_to_console else avg


avg = calculate_high_low_avg(1, 2, 3, 4, 5)
print(avg)
