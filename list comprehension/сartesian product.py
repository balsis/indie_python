colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']
lst = []

# for i in colors:
#     for j in sizes:
#         lst.append(i)

a = [(i, j) for i in colors for j in sizes]
print(a)