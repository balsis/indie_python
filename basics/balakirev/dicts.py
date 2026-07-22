lst_in = ['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm',
          'peremennyye-operator-prisvaivaniya-tipy-dannykh', 'arifmeticheskiye-operatsii',
          'ustanovka-i-poryadok-raboty-pycharm']

cache_values = {}

for i in lst_in:
    if i not in cache_values:
        value = f"HTML-страница для адреса {i}"
        cache_values[i] = value
        print(value)
    else:
        print(f'Взято из кэша: {cache_values[i]}')
