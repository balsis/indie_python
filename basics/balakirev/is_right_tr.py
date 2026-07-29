def is_right_tr(a, b, c, /, precision=0.001):
   check_1 = abs(c ** 2 - (a ** 2 + b ** 2)) < precision
   check_2 = abs(a ** 2 - (b ** 2 + c ** 2)) < precision
   check_3 = abs(b ** 2 - (a ** 2 + c ** 2)) < precision
   return check_1 or check_2 or check_3

res1 = is_right_tr(3, 4, 5, precision=0.01) # True
res2 = is_right_tr(3.00001, 4.0, 5.0) # True
res3 = is_right_tr(3.0, 4.001, 5.0) # False

assert res1 == True
assert res2 == True
assert res3 == False