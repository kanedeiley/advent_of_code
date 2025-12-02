from typing import Iterator, List, Tuple

invalid_id_sum = 0

def read_lines(path: str) -> List[str]:
    """Return all lines from path as a list of strings (no trailing newlines)."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

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

def split_into_chunks(s, chunk_size):
    """Split string s into chunks of length chunk_size."""
    return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]

p = "/Users/kane/Desktop/Advent of Code/2025/02/ids.txt"

lines = read_lines(p)
all_ranges = [t for line in lines for t in id_tuples(line)]

for id_range in all_ranges:
    for i in range(id_range[0], id_range[1] + 1):  # +1 to include the end
        s = str(i)
        length = len(s)
        is_invalid = False
        
        for j in range(1, length // 2 + 1):  # Check all possible chunk sizes
            if length % j == 0:  # Only check if evenly divisible
                chunks = split_into_chunks(s, j)
                if len(set(chunks)) == 1:  # All chunks are identical
                    is_invalid = True
                    break
        
        if is_invalid:
            invalid_id_sum += i
            print(f"{i} is invalid")

print(f"\nTotal: {invalid_id_sum}")