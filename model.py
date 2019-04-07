from dataclasses import dataclass
from typing import Tuple
from variables import MagnitudeValues

@dataclass
class Model:
    dependency: str
    value: MagnitudeValues
    Q1: Tuple[str, str]
    Q2: Tuple[str, str]
