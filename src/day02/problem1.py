import os


def find_repeats(start, end):
    repeats = []
    for n in range(start, end + 1):
        if n < 10:
            continue
        
        n_str = f'{n}'
        halfway = int(len(n_str)/2)
        #print(n_str, halfway)
        half_1 = n_str[0:halfway]
        whole = int(half_1 + half_1)
        if whole == n:
            repeats += [n]
    return repeats
        

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:
    result = 0
    repeats = []
    for line in file:
        ranges = line.split(',')
        for r in ranges:
            start, end = r.split('-')
            repeats += find_repeats(int(start), int(end))
    #print("Repeats", repeats)
    result = sum(repeats)
    print(result)
