import os

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'sample.txt')
with open(path, 'r') as file:

    