from string import ascii_lowercase

gen = (f"{i}{j}" for i in ascii_lowercase for j in ascii_lowercase)
for i in range(50):
    print(next(gen))