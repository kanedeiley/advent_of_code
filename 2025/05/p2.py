def is_overlapping(r1, r2):
    return r1[0] <= r2[1] + 1 and r2[0] <= r1[1] + 1

def merge_ranges(r1, r2):
    return (min(r1[0], r2[0]), max(r1[1], r2[1]))

ranges = []
with open('recipes.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line == "":
            break
        ranges.append(tuple(map(int, line.split('-'))))

ranges.sort()

merged = [ranges[0]]
for current in ranges[1:]:
    if is_overlapping(merged[-1], current):
        merged[-1] = merge_ranges(merged[-1], current)
    else:
        merged.append(current)

total = sum((end - start + 1) for start, end in merged)
print(total)