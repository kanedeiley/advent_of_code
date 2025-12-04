from collections import deque

roll_grid = []

with open('input.txt', 'r') as file:
    for line in file:
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

def get_neighbors(line, pos):
    """Get all valid neighbor coordinates"""
    neighbors = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            ny, nx = line + dy, pos + dx
            if 0 <= ny < roll_grid_height and 0 <= nx < roll_grid_width:
                neighbors.append((ny, nx))
    return neighbors

# Initial scan: find all accessible rolls
to_check = deque()
for l in range(roll_grid_height):
    for pos in range(roll_grid_width):
        if roll_grid[l][pos] == "@":
            if check_surroundings(l, pos) < 4:
                to_check.append((l, pos))

total_roll_hits = 0

# Process queue
while to_check:
    l, pos = to_check.popleft()
    
    # Double-check it's still a roll and still accessible
    if roll_grid[l][pos] != "@":
        continue
    if check_surroundings(l, pos) >= 4:
        continue
    
    # Remove this roll
    roll_grid[l][pos] = "."
    total_roll_hits += 1
    
    # Check all neighbors - they might now be accessible
    for ny, nx in get_neighbors(l, pos):
        if roll_grid[ny][nx] == "@" and check_surroundings(ny, nx) < 4:
            to_check.append((ny, nx))

print(total_roll_hits)