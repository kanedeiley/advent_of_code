from typing import Iterator, List, Tuple

invalid_id_sum = 0
id_list = []

def read_lines(path: str) -> List[str]:
    """Return all lines from path as a list of strings (no trailing newlines)."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def iter_lines(path: str) -> Iterator[str]:
    """Yield lines from path one by one (no trailing newlines)."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")

def id_tuples(line: str):
    out = []
    for part in line.split(","):
        p = part.strip()
        if not p:
            continue
        if "-" in p:
            start_s, end_s = p.split("-", 1)
            start, end = int(start_s), int(end_s)
            if end < start:
                raise ValueError(f"range end {end} < start {start}")
            out.append((start, end))
        else:
            n = int(p)
            out.append((n, n))
    return out


p = "/Users/kane/Desktop/Advent of Code/2025/02/ids.txt"

lines = read_lines(p)

all_ranges = [t for line in lines for t in id_tuples(line)]

for id_range in all_ranges:
    for i in range(id_range[0], id_range[1]):
        first = str(i)[:(len(str(i)) // 2)]
        second = str(i)[(len(str(i)) // 2):]
        if first == second:
            invalid_id_sum += i

print(invalid_id_sum)
        

