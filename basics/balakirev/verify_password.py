
russian = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"

def verify_password(psw, / , chars="@#!*", min_length=8):
        return (any(i for i in chars  if i in psw) and len(psw) >= min_length and
                all(char not in russian or char in chars or char.isdigit() for char in psw))


res1 = verify_password("fА12fgfhsf") # False
res2 = verify_password("VBNFGfdg!") # True
res3 = verify_password("VBNFGfdg!", min_length=15) # False
res4 = verify_password("VBNFGfdg!9", min_length=7, chars="@#$%^") # False


assert res1 == False and res2 == True and res3 == False and res4 == False