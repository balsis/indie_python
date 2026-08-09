try:
    with open("logs/01-01-2025/log_app.txt", encoding = "utf-8") as file:
        text = file.readlines()
        log_errors = [line.strip() for line in text if "ERROR" in line]
except FileNotFoundError:
    pass