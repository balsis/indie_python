check_word = lambda stroka: True if stroka.upper().startswith(start_letters) and stroka.upper().endswith(end_letters) else False
start_letters = ("Q", "R")
end_letters = ("A", "E", "I", "U", "O")

print(check_word.__name__)
print(check_word('radio'))