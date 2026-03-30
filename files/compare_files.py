def compare_files(filename1: str, filename2: str):
    file1, file2 = open(filename1), open(filename2)
    text1, text2 = file1.read(), file2.read()
    file1.close(), file2.close()
    return text1 == text2