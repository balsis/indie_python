def truncate_sentences(N, *phrases):
    for i in phrases:
        print(i[:N:])

truncate_sentences(
    8,
    "Мой дядя самых честных правил,",
    "Когда не в шутку занемог,",
    "Он уважать себя заставил"
)