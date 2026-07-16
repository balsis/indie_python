def check_hits(filename1, filename2):
    with open(filename1) as file1, open(filename2) as file2:
        text1 = set(file1.read().strip().split())
        text2 = set(file2.read().strip().split())
        return len((text1 & text2))


print(check_hits('shots_alpha.txt', 'ships_alpha.txt'))
