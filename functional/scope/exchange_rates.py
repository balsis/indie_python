exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}


def convert(currency_from, currency_to, amount):
    return round((exchange_rates[currency_to] / exchange_rates[currency_from]) * amount, 2)


currency = convert("EUR", "USD", 100)
print(currency)
