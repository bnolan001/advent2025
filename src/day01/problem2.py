import os

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'input.txt')
with open(path, 'r') as file:

    dial = 50
    password = 0
    for line in file:
        direction = line[0:1]
        clicks = int(line[1:])
        if clicks > 100:
            password += clicks // 100
            clicks = clicks % 100
        clicks = -1 * clicks if direction == 'L' else clicks
        movement = clicks + dial
        
        sign = (1 if movement > -1 else -1)
        
        # if we are already on 0 then don't count the movement
        if dial != 0:
            if movement > 99 or movement < 1:
                password += 1
                #print("Rotation", line.strip(), "Movement:", movement, "Password:", password)
                
        dial = (abs(movement)  % 100) * sign
        if dial < 0:
            dial += 100
        #print("Dial pointing to:", dial)

    print (password)
