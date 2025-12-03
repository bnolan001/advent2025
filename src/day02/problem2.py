import os


def find_repeats(start, end):
    repeats = []
    for n in range(start, end + 1):
        if n < 10:
            continue
        
        n_str = f'{n}'
        n_len = len(n_str)
        halfway = int(n_len/2)
        for h in range(halfway, 0, -1):

            if n_len % h != 0:
                continue
            times = int(n_len / h)
            sub_n = n_str[0:h]
            sub_n_whole = sub_n * times

            whole = int(sub_n_whole)

            if whole == n:
                repeats += [n]

    return set(repeats)
        

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:
    result = 0
    repeats = []
    for line in file:
        ranges = line.split(',')
        for r in ranges:
            start, end = r.split('-')
            repeats += list(find_repeats(int(start), int(end)))

    result = sum(repeats)
    print(result)
