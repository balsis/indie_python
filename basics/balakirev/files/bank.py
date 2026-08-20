try:
    with open("bank.csv", encoding = "utf-8") as file:
        text = file.readlines()
        row_data = {}
        first_row = text[0].split(",")
        second_row = text[1].split(",")
        le = len(first_row)
        for i in range(le):
            row_data[first_row[i].strip()] = second_row[i].strip()
except FileNotFoundError:
    pass