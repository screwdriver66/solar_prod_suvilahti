
# Preprocessors
The preprocessors are Scikit-learn-based custom transformers used to prepare the data for the pipeline. At the beginning of our pipeline our train.csv and test.csv had no NaN values prior to training due to how they were saved after the preprocessing jupyter notebook and due to the fact that you cannot drop NaN if you compel to Scikit-learn API, however you could impute them. Rows that absolutely had to be removed, were removed previously. During prediction, the validation function in validation.py (documentation link to validation.md) drops NaN's in the input data.

List of steps taken in the jupyter notebook:
- 1. Air and Dew-point temperature minssing values imputation from another file for a period during 2017-2018.
- 2. Dropping rows with NaN values in the rest of the data.
- 3. Target variable 2x outliers fixed

The preprocessing in the pipeline consists of the following steps:
- 1. Discretization
    - 1.1 Wind Direction is discretized into 16 bins segments 22.5 degrees each.
    - 1.2 Precipitation intensity into a binary variable, where 0 and 1 indicate no precipitation and precipitation, respectively.
    - 1.3 Cloud amount with the original values in [1/8] are discretized into a binary variable with 0 and 1 being cloud amount less than 5/8 and more or equal than that.

- 2. Adding additional features
    - 5.1 Hour of the day
    - 5.2 Day of the year
    - 5.3 Solar elevation angle
    - 5.4 Sun azimuth
    - 5.5 Theoretical global radiation

- 3. Drop unused features during training. ( Gust of wind speed, Snow depth, Horizontal visibility, datetime_converted )
- 4. Feature Scaling (optional). Added a Scikit-learn StandardScaler() transformer to scale the data in case some ML algorithms would require it. The original model on Random Forest Regressor does not require scaling, however a Neural Network-based model would, thus, the option is here.
