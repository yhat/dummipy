from .catpy import CategoricalDataFrame
import pandas
pandas.cDataFrame = CategoricalDataFrame
import os

__version__ = "0.0.1"

_ROOT = os.path.abspath(os.path.dirname(__file__))
cereal = pandas.read_csv(os.path.join(_ROOT, 'data', "cereal.csv"))
cereal = CategoricalDataFrame(cereal)
