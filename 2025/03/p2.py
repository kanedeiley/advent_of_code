max_ids = []

def get_max_id(battery):
    max_id = ""
    start_index = 0

    for digit_position in range(12):
        remaining_digits = 12 - digit_position

        search_end = len(battery) - remaining_digits + 1
        
        max_digit = max(battery[start_index:search_end])
        
        max_index = battery.find(max_digit, start_index, search_end)
        
        max_id += max_digit
        start_index = max_index + 1
        

    return max_id

with open('batteries.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()  
        max_ids.append(get_max_id(line))

print(max_ids)

print(sum([int(x) for x in max_ids]))
