import functools
from typing import Dict

from .parameters import PARAS


class RestrictedConfig:
    """
    A safe global config which can only be modified by the restricted methods.
    """

    def __init__(self):
        self.__config: dict = {}

    def restrict_to(self, func):
        def set_config(settings: Dict):
            self.__config.update(settings)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(set_config, *args, **kwargs)

        return wrapper

    @property
    def settings(self):
        return self.__config


Config = RestrictedConfig()


@Config.restrict_to
def _init_config(set_config):
    set_config(PARAS)


@Config.restrict_to
def update_config(set_config, new_config: Dict):
    set_config(new_config)
