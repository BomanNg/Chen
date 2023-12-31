import logging
import os
from pathlib import Path
from typing import List

import config

from Chen.modules import Cores, Dataset, Lab, Metrics

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Import private lab env
try:
    localLabEnv = ".lab.env"
    logger.info(f"Importing lab environment from {localLabEnv}")
    labEnv = Path("lab/" + localLabEnv, "r")
    with open(labEnv) as file:
        for line in file:
            key, value = line.strip().split("=", 1)
            os.environ[key] = value
except FileNotFoundError as e:
    logger.warning(f"Failed to load PATH. File '{localLabEnv}' not found.")


def run(scen: List[str], dataset, isMetric=True):
    # build clsCore
    clsCore = Cores(scen, config=config.LAB_CONFIG)

    # build test set
    testSet = Dataset(dataset)

    # run
    lab = Lab(clsCore, testSet, config=config.LAB_CONFIG)
    lab.apply()

    # metric
    if isMetric:
        metric = Metrics(lab, config=config.LAB_CONFIG)
        metric.apply()
