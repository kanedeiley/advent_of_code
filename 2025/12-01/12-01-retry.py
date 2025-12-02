# 6907 is the right answer

from typing import List, Tuple

# Starting dial position
current_dial: int = 50
total_zero_hits: int = 0

# Path to your spins file
p = "/Users/kane/Desktop/Advent of Code/2025/12-01/spins.txt"


def parse_line(line: str) -> Tuple[bool, int]:
    direction = line[0] == "R"
    spins = int(line[1:])
    return direction, spins

def get_current(current: int, spins: int, direction: bool):
    if direction:
        return (current + spins) % 100
    else:
        return (current - spins) % 100
    
def get_hits(current: int, spins: int, direction: bool):
    if direction:
        return (current + spins) // 100
    else:
        return ((current - 1) // 100) - ((current - spins - 1) // 100)

def update_dial(current: int, spins: int, direction: bool) -> Tuple[int, int]:
    return get_current(current, spins, direction), get_hits(current,spins,direction)

def process_spins(path: str) -> int:
    current_dial = 50
    total_zero_hits = 0
    
    with open(path, "r") as f:
        for line in f:
            direction, spins = parse_line(line.rstrip("\n"))
            current_dial, hits = update_dial(current_dial, spins, direction)
            total_zero_hits += hits
    
    return total_zero_hits

total_hits = process_spins(p)

print(f"(total hits) {total_hits}")