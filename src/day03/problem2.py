import os


def get_largest_joltage(num_str):
    
    unique_nums = list(set([char for char in num_str]))
    unique_nums.sort(reverse=True)
    largest = []
    prev_idx = 0
    
    while len(largest) != 12:
        restart = False
        for i in unique_nums:   
            i_str = str(i)
            while len(largest) < 12 and num_str.count(i_str, prev_idx) > 0:
                idx = num_str.index(i_str, prev_idx)
                if (len(num_str) - idx >= 12 - len(largest)):
                    largest += [num_str[idx]]
                    prev_idx = idx + 1
                    restart = True
                    break
                else:
                    break
            if restart:
                break

    print(largest)
    return int("".join(largest))

        

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:
    result = 0
    joltages = []
    for line in file:
        joltages += [get_largest_joltage(line.strip())]
    
    result = sum(joltages)
    print(result)
    