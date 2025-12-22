import json
import os
import copy

class BeamNode:
    def __init__(self, coords = None):
        self.left = None
        self.center = None
        self.right = None
        self.data = coords

# Helper function to display a 2D grid with spacing between rows
def print_map(map):
    for item in map:
        print(" ".join(item))
        print()

# Process beam paths through the grid, tracking splits when beams interact with '|' mirrors
def process_beams(data):
    # Create a deep copy to avoid modifying original data
    beams = copy.deepcopy(data)
    row_len = len(beams[0])
    beam_map = BeamNode()
    current_beams = []
    # Iterate through each row (except the last one)
    for i in range(0, len(beams) - 1):
        # Check if current row contains an up-facing beam (^)
        if '^' in beams[i]:
            new_beams = []
            s_idx = 0
            s_count = beams[i].count('^')
            
            # Process each ^ beam in this row
            for si in range(s_count):
                s_idx = beams[i].index('^', s_idx)
                
                # If beam hits a | mirror above and there's empty space to the left, split left
                if beams[i-1][s_idx] == '|' and s_idx > 0 and beams[i][s_idx - 1] != '^':
                    beams[i][s_idx - 1] = '|'
                    beam_node = BeamNode((i,s_idx - 1))
                    parent = (i-1, s_idx)
                    for cb in current_beams:
                        if cb.data == parent:
                            cb.left = beam_node
                    new_beams += [beam_node]
                
                # If beam hits a | mirror above and there's empty space to the right, split right
                if beams[i-1][s_idx] == '|' and s_idx < len(beams[i]) - 1 and beams[i][s_idx + 1] != '^':
                    beams[i][s_idx + 1] = '|'
                    beam_node = BeamNode((i,s_idx + 1))
                    parent = (i-1, s_idx)                    
                    for cb in current_beams:
                        if cb.data == parent:
                            cb.right = beam_node
                    new_beams += [beam_node]
              
                s_idx += 1
             
            
            # Propagate | beams from the row above downward where there's empty space
            for j in range(row_len):
                if beams[i-1][j] == '|' and beams[i][j] != '^':
                    beams[i][j] = beams[i-1][j]
                    beam_node = BeamNode((i,j))
                    parent = (i-1, j)   
                    for cb in current_beams:
                        if cb.data == parent:
                            cb.center = beam_node
                    new_beams += [beam_node]                    
                    
            current_beams = new_beams
                        
        # If row contains a source (S), create a beam going down
        elif 'S' in beams[i]:
            s_idx = beams[i].index('S')
            beams[i][s_idx] = '|'
            beam_map.data = (i, s_idx)
            current_beams += [beam_map]
            
        # If row is completely empty, propagate | beams from above
        else:
            new_beams = []
            for j in range(row_len):
                if beams[i-1][j] == '|':
                    beams[i][j] = beams[i-1][j]
                    beam_node = BeamNode((i,j))
                    parent = (i-1, j)   
                    for cb in current_beams:
                        if cb.data == parent:
                            cb.center = beam_node
                    new_beams += [beam_node]                    
                    
            if len(new_beams) > 0:
                current_beams = new_beams
    
    print("Total", len(current_beams))
    return (beam_map, beams)

def count_routes(beam):
    count = 0
    # utilize a cache to skip routes we already calculated
    if beam.data in cache:
        return cache[beam.data]
    if beam.left != None:
        count += count_routes(beam.left)
    if beam.center != None:
        count += count_routes(beam.center)
    if beam.right != None:
        count += 1
        count += count_routes(beam.right)
    cache[beam.data] = count
    return count

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
    (routes, beam_map) = process_beams(data)
    cache = {}
    result = count_routes(routes) + 1
    print(result) 
    