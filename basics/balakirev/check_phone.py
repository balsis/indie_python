def


res1 = check_phone("8(945)221-61-62") # True
res2 = check_phone("8(945)221-5007") # False
res3 = check_phone("+7(945)221-5007", "+7(xxx)xxx-xxxx") # True
res4 = check_phone('8(432)444-22-22', '8(xxx)xxx-xx-xx', format_symbol='*') # False
res5 = check_phone("+7(903)703-06-11", "+7(***)***-**-**", format_symbol='*') # True
res6 = check_phone("+7(***)*** ****", "+7(***)*** ****", format_symbol='*') # True

assert res1 == True
assert res2 == False
assert res3 == True
assert res4 == False
assert res5 == True
assert res6 == False