"""
Module containing the implementation of data object base class
"""

# Authors: Brannon Brakefield

from abc import ABC, abstractmethod
from calculations import Calculations

# =============================================================================
# Base data object
# =============================================================================


class DataObject(ABC):
    """Base, class for data objects

    Warning. This class should not be instantiated.
    """

    def __init__(self):
        self.calculator = Calculations()
        self.x = []
        self.y = []

    @abstractmethod
    def unpack_data(self):
        pass
