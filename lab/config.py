import json
from pathlib import Path

labConfig = Path("lab/labConfig.json")
with open(labConfig, "r") as file:
    LAB_CONFIG = json.load(file)

labTemp = Path("lab/labTemp.json")
with open(labTemp, "r") as file:
    LAB_TEMP = json.load(file)

SYSTEM = "system"
ASSISTANT = "assistant"
USER = "user"
TOOL = "tool"
