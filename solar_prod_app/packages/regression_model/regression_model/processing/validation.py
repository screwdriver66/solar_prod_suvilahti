from regression_model.config import config
import pandas as pd

def validate_inputs(input_data: pd.DataFrame) -> pd.DataFrame:
    '''Check model inputs for unprocessable values.'''

    validated_data = input_data.copy()
    # check for numerical variables with NA not seen during training
    # check for categorical variables with NA not seen during training
    # check for values <= 0 for the log transformed variables
    pass
