

def chunker(lst, chunk):
    first_index = 0
    while first_index < len(lst):
        last_index = first_index + chunk
        yield lst[first_index:last_index]
        first_index += chunk

for chunk in chunker(range(25), 4):
    print(list(chunk))


