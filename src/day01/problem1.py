import os

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:

    dial = 50
    password = 0
    for line in file:
        direction = line[0:1]
        clicks = int(line[1:])
        clicks = -1 * clicks if direction == 'L' else clicks
        movement = clicks + dial
        
        sign = (1 if movement > 0 else -1)
        dial = (abs(movement)  % 100) * sign
        password += 1 if dial == 0 else 0

    print (password)
