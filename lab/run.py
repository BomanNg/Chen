import logging
import os
from pathlib import Path
from typing import List

from lab import config
from modules import LLM, Cores, Dataset, Embedding

# Import private lab env
labEnv = Path('.lab.env', 'r')
with open(labEnv) as file:
    for line in file:
        key, value = line.strip().split('=', 1)
        os.environ[key] = value


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
