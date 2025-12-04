roll_grid = []

with open('input.txt', 'r') as file:
    for i, line in enumerate(file, 1):
        line = line.strip()
        roll_line = [x for x in line]
        roll_grid.append(roll_line)

roll_grid_height = len(roll_grid)
roll_grid_width = len(roll_grid[0])

def check_surroundings(line, pos):
    hits = 0
    adjacent = [(line + dy, pos + dx) 
            for dy in [-1, 0, 1] 
            for dx in [-1, 0, 1] 
            if not (dy == 0 and dx == 0)]
    
    for adj in adjacent:
        if (adj[0] < 0 or adj[0] >= roll_grid_height) or (adj[1] < 0 or adj[1] >= roll_grid_width):
            continue

        if roll_grid[adj[0]][adj[1]] == "@":
            hits += 1
    
    return hits


def get_hits_and_cords():
    roll_hits = 0
    cords = []
    for l in range(len(roll_grid)):
        for pos in range(len(roll_grid[l])):
            if roll_grid[l][pos] == "@":
                surrounding_hits = check_surroundings(l, pos)
                if surrounding_hits < 4:
                    roll_hits += 1
                    cords.append((l,pos))
    return roll_hits, cords

def replace_rolls(cords):
    for cord in cords:
        roll_grid[cord[0]][cord[1]] = "."

total_roll_hits = 0
checking = True

while checking:
    local_hits, cords = get_hits_and_cords()
    replace_rolls(cords)
    if local_hits == 0:
        break
    total_roll_hits += local_hits


print(total_roll_hits)