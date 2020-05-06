import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from regression_model.processing.errors import InvalidModelInputError

class NumericalImputer(BaseEstimator, TransformerMixin):
    '''Numerical missing values imputer for
        Air and Dew-point temperatures'''

    def  __init__(self, variables=None, reference_df=None):
        if not isinstance(variables, list):
            self.variables =  [variables]
        else:
            self.variables = variables

        self.reference_df = reference_df

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature].update(self.reference_df[feature], overwrite=False)
        return X

class WindDiscretizer(BaseEstimator, TransformerMixin):
    '''Discretization of Wind'''
    def __init__(self,  variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        buckets = np.arange(11.25, 372, 22.5)
        labels = np.arange(17)
        for feature in self.variables:
            X[feature][(X[feature]>=0)&(X[feature]<11.25)] = X[feature].apply(lambda x:x+360)
            X[feature]=labels[np.digitize(X[feature], buckets)]
        return X

class DiscretizerNumericalIntoBinary(BaseEstimator, TransformerMixin):
    '''Discretization of cloud coverage and precipitation intensity into binary'''
    def __init__(self, boundaries, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(X[feature]>self.boundaries[feature],1,0)
        return X

class TemporalVariableEstimatorHour(BaseEstimator, TransformerMixin):
    '''Hour'''
    def __init__(self, variables=None, reference_variable=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X.index.hour
        return X

class TemporalVariableEstimatorDay(BaseEstimator, TransformerMixin):
    '''Day'''
    def __init__(self, variables=None, reference_variable=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X.index.dayofyear
        return X

class SolarAngleEstimator(BaseEstimator, TransformerMixin):
    '''Calculating the solar angle'''
    def __init__(self, variables=None, reference_variable=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X.apply(lambda x: calc_alpha_s_for_df(N=x['day_of_year'],time=x['hour_of_day']),axis=1)
        return X

class SolarAzimuthEstimator(BaseEstimator, TransformerMixin):
    '''Calculating the solar angle'''
    def __init__(self, variables=None, reference_variable=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X.apply(lambda x: calc_sun_azimuth_for_df(N=x['day_of_year'],time=x['hour_of_day']),axis=1)
        return X


# how to engineer y_train outliers?
