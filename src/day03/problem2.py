import os


def get_largest_joltage(num_str):
    # Extract unique digits from the string and sort them in descending order
    # This allows us to prioritize larger digits when building the result
    unique_nums = list(set([char for char in num_str]))
    unique_nums.sort(reverse=True)
    
    # Initialize list to store the digits of the largest number
    largest = []
    # Track the current position in num_str to search from left to right
    prev_idx = 0
    
    # Build a 12-digit number by greedily selecting the largest available digits
    while len(largest) != 12:
        restart = False
        # Iterate through unique digits in descending order (largest first)
        for i in unique_nums:   
            i_str = str(i)
            # Search for the current digit in the remaining portion of num_str
            while len(largest) < 12 and num_str.count(i_str, prev_idx) > 0:
                idx = num_str.index(i_str, prev_idx)
                # Check if there are enough remaining characters to complete 12 digits
                if (len(num_str) - idx >= 12 - len(largest)):
                    # Add this digit to our result
                    largest += [num_str[idx]]
                    prev_idx = idx + 1
                    restart = True
                    break
                else:
                    # Not enough remaining characters, try next digit
                    break
            if restart:
                break

    print(largest)
    # Convert the list of digits into a single integer
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
    