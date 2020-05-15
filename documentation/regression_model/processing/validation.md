# Validation [source]

Validation is used to make sure that input data for predictionand does not contain NaNs in the feature set

> validate_inputs(input_data):

Functions takes input data in pandas.DataFrame object, drops __null__ values if there are any in the feature columns and returns __validated_data__

    Parameters- input_data: pandas.DataFrame object                         


    Outputs- pandas.DataFrame object
