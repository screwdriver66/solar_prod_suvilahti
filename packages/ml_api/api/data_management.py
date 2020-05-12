import pandas as pd
import joblib
from api import config
import logging

_logger = logging.getLogger(__name__)

def load_dataset(*, filename: str) -> pd.DataFrame:
    _data = pd.read_csv(f"{config.DATASET_DIR}/{filename}")
    _data = _data.set_index(pd.DatetimeIndex(pd.to_datetime(_data[config.DATETIME_INDEX], utc=True),dayfirst=True))
    return _data
