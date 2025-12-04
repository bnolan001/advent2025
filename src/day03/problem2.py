import os


def get_largest_joltage(num_str):
    joltage = ["0"] * 12
    largest = ["0"] * 12
    for a in range(len(num_str) - 11):
        joltage[0] = num_str[a]
        for b in range(a + 1,len(num_str) - 10):
            joltage[1] = num_str[b]
            for c in range(b + 1,len(num_str) - 9):
                joltage[2] = num_str[c]
                for d in range(c + 1,len(num_str) - 8):
                    joltage[3] = num_str[d]
                    for e in range(d + 1,len(num_str) - 7):
                        joltage[4] = num_str[e]
                        for f in range(e + 1, len(num_str) - 6):
                            joltage[5] = num_str[f]
                            for g in range(f + 1,len(num_str) - 5):
                                joltage[6] = num_str[g]
                                for h in range(g + 1,len(num_str) - 4):
                                    joltage[7] = num_str[h]
                                    for i in range(h + 1,len(num_str) - 3):
                                        joltage[8] = num_str[i]
                                        for j in range(i + 1,len(num_str) - 2):
                                            joltage[9] = num_str[j]
                                            for k in range(j + 1, len(num_str) - 1):
                                                joltage[10] = num_str[k]
                                                for l in range(k + 1,len(num_str)):
                                                    joltage[11] = num_str[l]
                                                    if joltage > largest:
                                                        largest = list(joltage)

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
    