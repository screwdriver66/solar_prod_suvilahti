# Solar calculation functions [source](https://github.com/screwdriver66/solar_prod_suvilahti/blob/master/packages/solar_prod_suvilahti_ml_model/regression_model/processing/solar_calculation_functions.py)

This file contains a collection of functions related to calculation of theoretical maximum available solar radiation and several other features used in the model. The source for these formulae
is from chapter 2 of [Photovoltaic power generation modeling report by H.-P. Hellman, 2011](http://sgemfinalreport.fi/files/WP611_photovoltaics%20HP%20Hellman.pdf).

These features reflect the temporal and seasonal dependency that has to be reflected in our model. These temporal and seasonal dependencies are due to position of the Sun in different days and months in relation to the observer. The following features are calculated for our regression model:

1. Solar elevation angle - the angle between the horizon and the centre of the Sun's disc.
2. Sun azimuth - defined as the angle between the projection of sun’s centre onto the horizontal plane and due south direction
  ([source](https://www.sciencedirect.com/topics/engineering/solar-azimuth-angle)).
3. Theoretical maximum solar radiation (under clear sky)

The following variables and assumptions are taken during the calculation:

1. longtitude = 24.9693
2. latitude = 60.1867
3. PV panel azimuth - 0 degrees (panel facing south)
4. Inclination of the panels - 45 degrees (the usual value for northern countries)
