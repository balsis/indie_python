def check_a_in_str(phrase):
    result = [True if "a" in i.lower() else False for i in phrase.split()]
    return all(result)


print(check_a_in_str("chase enlarge referee cup offense"))
print(check_a_in_str("acquaintance disAgree"))