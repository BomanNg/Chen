import logging
import os
from pathlib import Path
from typing import List

from lab import config
from modules import LLM, Cores, Dataset, Embedding

labLogger = logging.getLogger("LabLogger")
dataLogger = logging.getLogger("DataLogger")

# Import private lab env
localLabEnv = ".lab.env"
try:
    labLogger.info(f"Importing lab environment from {localLabEnv}")
    labEnv = Path(localLabEnv, "r")
    with open(labEnv) as file:
        for line in file:
            key, value = line.strip().split("=", 1)
            os.environ[key] = value
except FileNotFoundError as e:
    labLogger.warning(f"Failed to load PATH. File '{localLabEnv}' not found.")


def apply():
    ...


def metric():
    ...


def runLab(scen: List[str], dataset):
    llm = LLM()
    embedding = Embedding()

    # build clsCore
    clsCore = Cores(scen, llm, embedding)

    # build test set
    testSet = Dataset(dataset)

    # run
    apply(clsCore, testSet, embedding)

    # metric
    logPath = Path()
    metric(logPath)
