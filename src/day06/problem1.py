import os
import math

def print_map(map):
    for item in map:
        print(" ".join(item))
        
def run_calculation(data):
    totals = []
    for d in data:
        d_sub = d[0:len(d) - 1]
        if d[len(d) - 1] == '+':
            totals += [sum(d_sub)]
        if d[len(d) - 1] == '-':
            d_sub *= -1
            totals += [sum(d_sub)]
        if d[len(d) - 1] == '*':
            totals += [math.prod(d_sub)]
    return totals


script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:
    result = 0
    data = []
    for line in file:
        values = line.strip().split()
        
        for i in range(len(values)):
            if (len(data) <= i):
                data += [[]]
            data[i] += [int(values[i])] if values[i].isnumeric() else [values[i]]
            
    totals = run_calculation(data)
    result = sum(totals)
    print(result)
    