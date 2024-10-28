def translate_to_robber_lang(phrase):
    vowels = {"a", "e", "i", "o", "u"}
    return ''.join(
        [f'{letter}o{letter}' if letter.isalpha() and letter.lower() not in vowels else letter for letter in phrase]
    )


print(translate_to_robber_lang("This is kinda fun"))

# assert translate_to_robber_lang("This is kinda fun") == "ToThohisos isos kokinondoda fofunon"
# assert translate_to_robber_lang("I Think YoU Might BE righT!") == "I ToThohinonkok YoYoU MoMigoghohtot BoBE rorigoghohToT!"
