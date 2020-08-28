import importlib
import os
from collections import namedtuple
import torch


def load_ext(name, funcs):
    ext = importlib.import_module('ops_lib.' + name)
    for fun in funcs:
        assert hasattr(ext, fun), f'{fun} miss in module {name}'
    return ext
