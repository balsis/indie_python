def from_hex_to_rgb(color: str) -> tuple[int, int, int]:
    color = color.lstrip('#')
    r = int(color[0:2], 16)  # Красный
    g = int(color[2:4], 16)  # Зеленый
    b = int(color[4:6], 16)

    return r, g, b


def convert_to_rgb(hex_colors):
    return [from_hex_to_rgb(color) for color in hex_colors]


colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50']
print(convert_to_rgb(colors))