sale_lambda = lambda x: x * 0.9 if x > 50 else x


print(sale_lambda.__name__)
print(sale_lambda(60))
