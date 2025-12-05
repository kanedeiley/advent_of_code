ranges = []
ingredients = []
is_range = True
fresh = 0

with open('recipes.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line == "":
            is_range = False
            continue

        if is_range:
            ranges.append(tuple(map(int, line.split('-'))))

        else:
            ingredients.append(int(line))

for i in ingredients:
    for r in ranges:
        if r[0] <= i <= r[1]:
            fresh += 1
            break

print(fresh)
