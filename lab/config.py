import json
from pathlib import Path

labConfig = Path('labConfig.json')
with open(labConfig, 'r') as file:
    LAB_CONFIG = json.load(file)

labTemp = Path('labTemp.json')
with open(labTemp, 'r') as file:
    LAB_TEMP = json.load(file)
