import os

def print_map(map):
    for item in map:
        print(" ".join(item))
        
def count_rolls(map):
    roll_count = 0
    for i in range(1, len(map) - 1):
        for j in range(1, len(map[i]) - 1):
            if map[i][j] == '@':
                nbr_rolls = 0
                nbr_rolls += 1 if map[i-1][j-1] != '.' else 0
                nbr_rolls += 1 if map[i-1][j] != '.' else 0
                nbr_rolls += 1 if map[i-1][j+1] != '.' else 0
                nbr_rolls += 1 if map[i][j-1] != '.' else 0
                nbr_rolls += 1 if map[i][j+1] != '.' else 0
                nbr_rolls += 1 if map[i+1][j-1] != '.' else 0
                nbr_rolls += 1 if map[i+1][j] != '.' else 0
                nbr_rolls += 1 if map[i+1][j+1] != '.' else 0

                if nbr_rolls < 4:
                    roll_count += 1
                    map[i][j] = '.'

    return roll_count

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:
    result = 0
    map = []
    for line in file:
        map += [list("."+line.strip()+".")]
    
    map += [["."] * len(map[0])]
    map.insert(0, ["."] * len(map[0]))

    #print_map(map)

    count = 1
    while(count > 0):
        count = count_rolls(map)
        result += count
    #print("------------------")
    #print_map(map)

    print(result)
    