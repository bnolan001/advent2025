import os
import copy

import os
import copy

# Helper function to display a 2D grid with spacing between rows
def print_map(map):
    for item in map:
        print(" ".join(item))
        print()

# Process beam paths through the grid, tracking splits when beams interact with '|' mirrors
def process_beams(data):
    # Create a deep copy to avoid modifying original data
    beams = copy.deepcopy(data)
    splits = 0
    row_len = len(beams[0])
    
    # Iterate through each row (except the last one)
    for i in range(0, len(beams) - 1):
        # Check if current row contains an up-facing beam (^)
        if '^' in beams[i]:
            s_idx = 0
            s_count = beams[i].count('^')
            
            # Process each ^ beam in this row
            for si in range(s_count):
                s_idx = beams[i].index('^', s_idx)
                beam_split = False
                
                # If beam hits a | mirror above and there's empty space to the left, split left
                if beams[i-1][s_idx] == '|' and s_idx > 0 and beams[i][s_idx - 1] == '.':
                    beam_split = True
                    beams[i][s_idx - 1] = '|'
                
                # If beam hits a | mirror above and there's empty space to the right, split right
                if beams[i-1][s_idx] == '|' and s_idx < len(beams[i]) - 1 and beams[i][s_idx + 1] == '.':
                    beam_split = True
                    beams[i][s_idx + 1] = '|'
                
                s_idx += 1
                splits += 1 if beam_split else 0
            
            # Propagate | beams from the row above downward where there's empty space
            for j in range(row_len):
                if beams[i-1][j] == '|' and beams[i][j] == '.':
                    beams[i][j] = beams[i-1][j]
        
        # If row is completely empty, propagate | beams from above
        elif beams[i].count('.') == row_len:
            for j in range(row_len):
                if beams[i-1][j] == '|':
                    beams[i][j] = beams[i-1][j]
        
        # If row contains a source (S), create a beam going down
        elif 'S' in beams[i]:
            s_idx = beams[i].index('S')
            beams[i+1][s_idx] = '|'
    
    return splits



script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')

# Read input file and process beam interactions
with open(path, 'r') as file:
    result = -1
    data = []
    
    # Read each line and convert to list of characters
    for line in file:
        values = list(line.strip())
        data += [values]
    
    # Process the beam data and count splits
    result = process_beams(data)
    print(result) 
    