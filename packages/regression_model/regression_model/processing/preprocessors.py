import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from regression_model.processing.errors import InvalidModelInputError
from regression_model.processing.azimuth_one_script import *
# PUT THESE IN ANOTHER SCRIPT
longtitude = 24.9693
latitude = 60.1867
delta_GMT = 3
def calc_sun_azimuth_for_df(N, time, lon=longtitude, delta_GMT=3, phi=latitude):
    delta = calc_delta(N)
    omega = calc_omega(N, lon, delta_GMT, time)
    alpha_s = calc_alpha_s(phi, delta, omega)
    gamma_s = calc_gamma_s(alpha_s, phi, delta, omega)
    return gamma_s

def calc_alpha_s_for_df(N, time, lon=longtitude, delta_GMT=3, phi=latitude):
    delta = calc_delta(N)
    omega = calc_omega(N, lon, delta_GMT, time)
    alpha_s = calc_alpha_s(phi, delta, omega)
    return alpha_s
###

# List of all preprocessor steps:
# 1. Air and Dew-point temperature minssing values imputation from another file
#    for a period.
# 2. Dropping NA in the rest of the data.
# 3. Target variable 2x outliers fixed
#maybe 1, 2 and 3 should be done outside of the pipeline
# ----- DONE -----
# the file with first 3 done is ../datasets/pipeline_df.csv

# 4. Discretization
#   4.1 Wind Direction into bins and bin-number-categories
#   4.2 Precipitation intensity -> binary 0,1
#   4.3 Cloud amount -> binary <5 == 0, >=5 ==1

# column transformers on these?
# ----- DONE -----

# 5. Additional features
#   5.1 Hour of the day
#   5.2 Day of the year
#   5.3 Solar elevation angle
#   5.4 Sun azimuth
#   5.5 Theoretical global radiation

# 6. Drop features: Gust of wind, Snow depth, Horizontal visibility, datetime
# 7. Scale (StandardScaler)

class WindDiscretizer(BaseEstimator, TransformerMixin):
    '''Discretization of Wind'''
    def __init__(self,  variable=None):
        self.variable = variable

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        buckets = np.arange(11.25, 372, 22.5)
        labels = np.arange(17)
        X[self.variable].loc[(X[self.variable]>=0)&(X[self.variable]<11.25)] = X[self.variable].loc[(X[self.variable]>=0)&(X[self.variable]<11.25)].apply(lambda x:x+360)
        X[self.variable]=labels[np.digitize(X[self.variable], buckets)]
        return X

class DiscretizerNumericalIntoBinary(BaseEstimator, TransformerMixin):
    '''Discretization of cloud coverage and precipitation intensity into
        binary. The function takes a dictionary of variables as boundaries.
    '''

    def __init__(self, boundaries=None, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
        self.boundaries=boundaries

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(X[feature]>self.boundaries[feature],1,0)
        return X

class TemporalHour(BaseEstimator, TransformerMixin):
        #remove for loop in the transform
        def __init__(self, variable=None, ref_feature=None):
            self.variable = variable
            self.ref_feature = ref_feature
            #can make one temporal transformer for both issues
            #dict with lambda?

        def fit(self, X, y=None):
            return self

        def transform(self, X):
            X = X.copy()
            X[self.variable] = pd.DatetimeIndex(pd.to_datetime(X[self.ref_feature])).hour
            return X

class TemporalDayofYear(BaseEstimator, TransformerMixin):
        #remove for loop in the transform
        def __init__(self, variable=None, ref_feature=None):
            self.variable = variable
            self.ref_feature = ref_feature

        def fit(self, X, y=None):
            return self

        def transform(self, X):
            X = X.copy()
            X[self.variable] = pd.DatetimeIndex(pd.to_datetime(X[self.ref_feature])).dayofyear
            return X


class SolarElevAngle(BaseEstimator, TransformerMixin):

        def __init__(self, var_name=None, day=None, hour=None):
            self.var_name = var_name
            self.day = day
            self.hour = hour

        def fit(self, X, y=None):
            return self

        def transform(self, X):
            X = X.copy()
            X[self.var_name] = X.apply(lambda x: calc_alpha_s_for_df(N=x[self.day],time=x[self.hour]),axis=1)

            return X

class SunAzimuth(BaseEstimator, TransformerMixin):

        def __init__(self, var_name=None, day=None, hour=None):
            self.var_name = var_name
            self.day = day
            self.hour = hour

        def fit(self, X, y=None):
            return self

        def transform(self, X):
            X = X.copy()
            X[self.var_name] = X.apply(lambda x: calc_sun_azimuth_for_df(N=x[self.day],time=x[self.day]),axis=1)

            return X

class DropUnnecessaryFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None):
        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X = X.drop(self.variables, axis=1)

        return X
