# Solar Production Suvilahti Machine Learning Application

This is an end-to-end machine learning project that provides hourly prediction of produced energy at Suvilahti PV plant for the upcoming 36 hours. Prediction values are obtained through a regression model that utilizes the Finnish Meteorological Institute (FMI) open data and weather API as input parameters.

## Description

The goal of the project was to choose a dataset that was not yet popular in tutorials, create a ML model and to deploy it in production. The processes covered in the project can be subdivided into the following steps:

- Research - problem statement, gathering tools, data and creating a vision of the solution. Carried out in Jupyter notebooks.
- Development environment - translating solutions from research environment to development. This includes utilizing Scikit-learn API feature engineering transformers, creating custom transformers and creating a pipeline for regression model training. Additionally, it covers unit testing, validation of input data and training the regression model.

- ML Application - testing and packaging the regression model as a python package and hosting it on an index server. Currently the package is hosted on pypi.org [source](https://pypi.org/project/solar-prod-suvilahti-ml-model/) .
- Model API - serving the model through REST API to serve our predictions and showcase the visualization as the result of the model predcition. API is utilized to decouple model development from the client facing layer. It would allow to later combine multiple models to be served at different API endpoints with a possibility to scale. The API is deployed through a Flask application that is run in a Docker container on Heroku, utilizing also the Gunicorn WSGI HTTP Server.
- CI/CD - Continuous Integration Continuous Deployment, sometimes interchangibly used with Delivery, allows to automate the development stages. This is done by automatically testing the code and as soon as the code is merged with a feature branch to automatically release the code to either production or a testing environemnt. In this project this is done via CircleCI.


 Monitoring of the quality of model predictions after deployment and more elaborated testing is coming in next updates.

## API

Get the prediction values from the regression model either in a POST request or use the GET method to view predictions in a rendered HTML page visualized in the bar chart. [[source](https://github.com/screwdriver66/solar_prod_suvilahti/blob/master/documentation/api.md)]

<!-- ## Regression model package installation
You can configure your Python project to use Gemfury as the primary source of packages. To start, add Gemfury as the main index to the top of your project’s requirements.txt:

CONFIGURE THIS! -->

## Documentation

Documentation can be found in [[source](https://github.com/screwdriver66/solar_prod_suvilahti/tree/master/documentation)]

## Jupyter notebooks

- Data gathering [[source]()]
- Data analysis [[source]()]
- Feature engineering [[source]()]
- Model building [[source]()]

## Licenses

- The source code is under the GNU GPL v3 license [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

- Weather observation part of the data set, downloaded from https://en.ilmatieteenlaitos.fi/open-data, prior to its modification is under [Creative Commons Attribution 4.0 International
License][cc-by]. [![CC BY 4.0][cc-by-shield]][cc-by]

- Solar energy production part of the data set was downloaded from https://www.helen.fi/en/solar-panels/solar-power-plants/suvilahti-solar-power-plant prior to its modification had no license document on the web page.

The aforementioned datasets were used in model training and testing. The modified versions are located in regression model's package [datasets](/packages/regression_model/regression_model/datasets/) folder.



[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
