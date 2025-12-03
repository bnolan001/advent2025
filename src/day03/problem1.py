import os


def get_largest_joltage(num_str):
    unique_nums = list(set([int(char) for char in num_str]))
    unique_nums.sort(reverse=True)

    max_num = [0, 0]
    for i in unique_nums:
        idx_1 = num_str.index(str(i))
        for j in unique_nums:
            if num_str.rindex(str(j)) > idx_1 and max_num < [i, j]:
                max_num = [i, j]
                    
    print(max_num)
    return max_num[0] * 10 + max_num[1] 

        

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:
    result = 0
    joltages = []
    for line in file:
        joltages += [get_largest_joltage(line.strip())]
    
    result = sum(joltages)
    print(result)
    