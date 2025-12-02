from typing import List, Tuple
import math

# Starting dial position
current_dial: int = 50
total_zero_hits: int = 0

# Path to your spins file
p = "/Users/kane/Desktop/Advent of Code/2025/12-01/spins.txt"

def read_lines(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def parse_line(line: str) -> Tuple[bool, int]:
    direction = line[0] == "R"
    spins = int(line[1:])
    return direction, spins

def update_dial(current: int, spins: int, direction: bool) -> Tuple[int, int]:
    """
    Move the dial one click at a time and count exact zero hits.
    """
    zero_hits = 0
    for _ in range(spins):
        # Move one step
        if direction:
            current = (current + 1) % 100
        else:
            current = (current - 1) % 100
        
        if current == 0:
            zero_hits += 1

    return current, zero_hits

# Read the spins
lines = read_lines(p)


# Process each spin
for line in lines:
    direction, spins = parse_line(line)
    current_dial, hits = update_dial(current_dial, spins, direction)
    total_zero_hits += hits

print("Password (total zero hits):", total_zero_hits)
