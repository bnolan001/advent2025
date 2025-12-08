import os

def print_map(map):
    for item in map:
        print(" ".join(item))
        
def get_found_count(ranges, tests):
    total_count = 0
    for t in tests:
        for r in ranges:
            if r[0] <= t <= r[1]:
                total_count += 1
                break
    return total_count

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:
    result = 0
    ranges = []
    tests = []
    rangeLine = True
    for line in file:
        if line.strip() == '':
            rangeLine = False
            continue

        if rangeLine:
            nums = line.strip().split('-')
            r = [int(nums[0]), int(nums[1])]
            ranges += [r]
        else:
            tests += [int(line.strip())]
            
    result = get_found_count(ranges, tests)

    print(result)
    