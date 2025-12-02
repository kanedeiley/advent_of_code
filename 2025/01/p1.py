# ...existing code...
from typing import Iterator, List

current_dial: int = 50
passed_zero_count: int = 0

def read_lines(path: str) -> List[str]:
    """Return all lines from path as a list of strings (no trailing newlines)."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def iter_lines(path: str) -> Iterator[str]:
    """Yield lines from path one by one (no trailing newlines)."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")

def strip_directions(s: str):
    return s[0] == "R", int(s[1:])


def update_dial(current: int, spins: int, direction: bool):
    if direction:
        current = current + spins
    else:
        current = current - spins
    return current, ((abs(current) % 100) == 0)



p = "/Users/kane/Desktop/Advent of Code/2025/12-01/spins.txt"
lines = read_lines(p)

for line in lines:
    pos, spins = strip_directions(line)
    current_dial, is_zero = update_dial(current_dial, spins, pos)
    print(current_dial, is_zero)
    if is_zero:
        passed_zero_count += 1

print(passed_zero_count)





