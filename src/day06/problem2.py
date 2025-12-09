import os
import math

# Helper function to display a 2D map/grid
def print_map(map):
    for item in map:
        print(" ".join(item))

# Parse input data to extract numbers and operators into separate groups
def organize_data(data):
    # Initialize structure to hold parsed groups of numbers and operators
    organized_data = [[]]
    organized_data_index = 0
    operator = ''
    
    for i in range(len(data)):
        line = ''.join(data[i]).strip()
        
        # Empty line signals end of a group, store the operator and start new group
        if line == '':
            organized_data[organized_data_index] += [operator]
            organized_data += [[]]
            organized_data_index += 1
        # Line contains number and operator (e.g., "123+"), extract both
        elif not line.isnumeric():
            num = line[0:len(line)-1]
            organized_data[organized_data_index] += [int(num)]
            operator = line[-1]
        # Line is purely numeric, add as integer to current group
        elif line.isnumeric():
            organized_data[organized_data_index] += [int(line)]

    return organized_data[:-1]

def run_calculation(data):
    # Process each group of numbers with their corresponding operator
    totals = []
    for d in data:
        # Extract all numbers from the group (all but the last element which is the operator)
        d_sub = d[0:len(d) - 1]
        
        # Apply the operator and store the result
        if d[len(d) - 1] == '+':
            totals += [sum(d_sub)]
        if d[len(d) - 1] == '-':
            # For subtraction, negate all values then sum
            d_sub *= -1
            totals += [sum(d_sub)]
        if d[len(d) - 1] == '*':
            # For multiplication, compute the product of all values
            totals += [math.prod(d_sub)]
    return totals


script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')

# Read input file and process data
with open(path, 'r') as file:
    result = 0
    data = []
    
    # Read file line by line, converting each to a list of characters
    for line in file:
        data += [list(line)]
    
    # Rotate data 90 degrees counterclockwise: reverse rows then transpose
    rotated_data = [list(row) for row in zip(*data[::-1])]
    
    # Mirror the rotated data horizontally
    mirrored_data = [list(row[::-1]) for row in rotated_data[::]]
    
    # Parse the transformed data to extract numbers and operators
    orged_data = organize_data(mirrored_data)
    
    # Calculate results for each group based on their operator
    totals = run_calculation(orged_data)
    
    # Sum all results and print the final answer
    result = sum(totals)
    print(result)
    