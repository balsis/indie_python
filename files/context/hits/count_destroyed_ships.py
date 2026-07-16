def count_destroyed_ships(ships_file, shots_file):
    with open(ships_file) as ships_file, open(shots_file) as shots_file:
        count = 0
        ships = [set(text.split()) for text in ships_file.read().split("\n\n")]
        shots = set(shots_file.read().strip().split())
        for ship in ships:
            if (ship & shots) == ship:
                count += 1
        return count


print(count_destroyed_ships('ships_1.txt', 'shots_1.txt', ))
