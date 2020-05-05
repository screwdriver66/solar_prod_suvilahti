import pathlib

import regression_model # where is this???

import pandas as pd

pd.options.display.max_rows = 10
pd.options.display.max_columns = 10

PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
print(PACKAGE_ROOT)
