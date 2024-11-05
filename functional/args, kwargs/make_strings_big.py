def make_strings_big(*args, reverse=False):
    if reverse:
        for i in args:
            print(i.lower())
    else:
        for i in args:
            print(i.upper())


make_strings_big('У лукоморья дуб зелёный',
                     'Златая цепь на дубе том:',
                     'И днём и ночью кот учёный')

make_strings_big('У лукоморья дуб зелёный',
                     'Златая цепь на дубе том:',
                     'И днём и ночью кот учёный', reverse = True)