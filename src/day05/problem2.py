import os
import copy 

def print_map(map):
    for item in map:
        print(" ".join(item))
        
def merge_ranges(ranges):
    ranges_to_merge = copy.deepcopy(ranges)
    total_merged = 1
    # Sort the starting of the range
    sorted(ranges_to_merge, key=lambda x: x[0])
    merged = []
    while total_merged != 0:
        total_merged = 0
        for r in ranges_to_merge:
            new_range = True
        
            for m in merged:
                if r[0] >= m[0] and r[1] <= m[1]:
                    new_range = False
                    break
                # r starts at or before m and r ends at or after m
                if r[0] <= m[0] and r[1] >= m[0]:
                    new_range = False
                    m[0] = r[0]
                    if r[1] > m[1]:
                        m[1] = r[1]
                    total_merged += 1
                    break
                # r stats at or before end of m and ends at or after m
                elif r[0] <= m[1] and r[1] >= m[1]:
                    new_range = False
                    m[1] = r[1]
                    if r[0] < m[0]:
                        m[0] = r[0]
                        total_merged += 1
                        break
            # r is a new range that should be added
            if new_range:
                merged += [r]
        ranges_to_merge = copy.deepcopy(merged)
        merged = []
                
            
    return ranges_to_merge

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:
    result = 0
    ranges = []
    tests = []
    rangeLine = True
    for line in file:
        if line.strip() == '':
            break

        if rangeLine:
            nums = line.strip().split('-')
            r = [int(nums[0]), int(nums[1])]
            ranges += [r]
            
    merged = merge_ranges(ranges)
    result = 0
    for m in merged:
        result += m[1] - m[0] + 1

    print(result)
    