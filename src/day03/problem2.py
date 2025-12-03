import os


def get_largest_joltage(num_str):
    return 0

        

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:
    result = 0
    joltages = []
    for line in file:
        joltages += [get_largest_joltage(line.strip())]
    
    result = sum(joltages)
    print(result)
    