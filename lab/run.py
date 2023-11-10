import os
from pathlib import Path

# Import private lab env
labEnv = Path('.lab.env', 'r')
with open(labEnv) as file:
    for line in file:
        key, value = line.strip().split('=', 1)
        os.environ[key] = value
