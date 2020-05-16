# Pipeline

Regression model pipeline used for feature preprocessing prior to training the model or making predictions.

1. Pipeline [[source](https://github.com/screwdriver66/solar_prod_suvilahti/blob/master/packages/solar_prod_suvilahti_ml_model/regression_model/pipeline.py)] - The preprocessors are described in Preprocessors [[source](https://github.com/screwdriver66/solar_prod_suvilahti/blob/master/documentation/regression_model/preprocessors.md)]
2. Train pipeline [[source](https://github.com/screwdriver66/solar_prod_suvilahti/blob/master/packages/solar_prod_suvilahti_ml_model/regression_model/train_pipeline.py)]
3. Predict [[source](https://github.com/screwdriver66/solar_prod_suvilahti/blob/master/packages/solar_prod_suvilahti_ml_model/regression_model/predict.py)]


> train_pipeline.run_training():

The function:
1. Loads the training data set from __regression_model/datasets/__
2. Performs sklear.model_selection.train_test_split
3. Performs pipeline.fit() method
4. Saves the trained model pipeline in __regression_model/trained_models/__

> predict.make_prediction(input_data):

Makes prediction using the saved model pipeline.

    Parameters- input_data: pandas.DataFrame object                         


    Outputs- python dict with keys:
            "predictions" : predictions - python list of floats
            "version"     : _version    - model version
