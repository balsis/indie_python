def is_adult(age):
    return age >= 18

a = int(input())
if is_adult(a):
    print('Ух какой большой')
else:
    print('Подрасти еще, сынок')