def generate_id_list(id):
    id_list = []
    for i in range(len(id) -1):
        for j in range(i + 1, len(id)):
            id_list.append(str(id[i]) + str(id[j]))
    return id_list

def max_id_in_list(id_list):   
    max_id = max([int(x) for x in id_list])
    return max_id

max_ids = []

with open('batteries.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()  

with open('batteries.txt', 'r') as file:
    for line in file:
        line = line.strip()

with open('batteries.txt', 'r') as file:
    for i, line in enumerate(file, 1):
        line = line.strip()
        id_list = generate_id_list(line)
        max_id = max_id_in_list(id_list)
        max_ids.append(max_id)

print("Max IDs:", max_ids)
print(sum(max_ids))
