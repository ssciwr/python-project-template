
from importlib import metadata

__version__ = metadata.version(__package__)
del metadata

def add_one(x: int):
    """An example function that increases a number

    :param x: The input parameter to increase
    :return: The successor of the given number
    """
    return x + 1
