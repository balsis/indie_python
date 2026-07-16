rect_width, rect_height, w, h = 640, 480, 23, 44

#
is_ostatok_shirina = rect_width % w > 0
is_ostatok_vysota = rect_height % h > 0
print(is_ostatok_shirina, is_ostatok_vysota)

vsego_cel_plitok_shirina = rect_width // w
vsego_cel_plitok_vysota = rect_height // h
print(vsego_cel_plitok_shirina, vsego_cel_plitok_vysota)

total = vsego_cel_plitok_shirina * is_ostatok_vysota + vsego_cel_plitok_vysota * is_ostatok_shirina + (is_ostatok_shirina * is_ostatok_vysota)

print(total)

#  Неверное значение переменной total для следующих чисел rect_width, rect_height, w, h:
#  (640, 480, 23, 44). Должно получиться 38, а у вас 60.