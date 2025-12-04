import os


def get_largest_joltage(num_str):
    joltage = ["0"] * 12
    largest = ["0"] * 12
    for a in range(len(num_str) - 12):
        joltage[0] = num_str[a]
        for b in range(a + 1,len(num_str) - 11 - a):
            joltage[1] = num_str[b]
            for c in range(b + 1,len(num_str) - 10 - b):
                joltage[2] = num_str[c]
                for d in range(c + 1,len(num_str) - 9 - c):
                    joltage[3] = num_str[d]
                    for e in range(d + 1,len(num_str) - 8 - d):
                        joltage[4] = num_str[e]
                        for f in range(e + 1, len(num_str) - 7 - e):
                            joltage[5] = num_str[f]
                            for g in range(f + 1,len(num_str) - 6 - f):
                                joltage[6] = num_str[g]
                                for h in range(g + 1,len(num_str) - 5 - g):
                                    joltage[7] = num_str[h]
                                    for i in range(h + 1,len(num_str) - 4 - h):
                                        joltage[8] = num_str[i]
                                        for j in range(i + 1,len(num_str) - 3 - i):
                                            joltage[9] = num_str[j]
                                            for k in range(j + 1, len(num_str) - 2 - j):
                                                joltage[10] = num_str[k]
                                                for l in range(k + 1,len(num_str) - 1 - k):
                                                    joltage[11] = num_str[l]
                                                    if joltage > largest:
                                                        largest = joltage

    print(largest)
    return int("".join(largest))

        

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'sample.txt')
with open(path, 'r') as file:
    result = 0
    joltages = []
    for line in file:
        joltages += [get_largest_joltage(line.strip())]
    
    result = sum(joltages)
    print(result)
    