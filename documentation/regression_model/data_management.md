# Data management [source](https://github.com/screwdriver66/solar_prod_suvilahti/blob/master/packages/solar_prod_suvilahti_ml_model/regression_model/processing/data_management.py)

Data management includes the following functions:
- Load a data set
- Save a pipeline (includes removing any old pipelines)
- Load a pipeline



> load_dataset(filename):

Functions loads the dataset from a specified filepath into a pandas DataFrame object, setting the index to
pandas DatetimeIndex.

    Parameters- filename: str                          
                Path to the file.

    Outputs- pandas.DataFrame object with DatetimeIndex

> save_pipeline(pipeline_to_persist):

Saves the versioned model, and overwrites any previous saved models. This ensures that when the package is
  published, there is only one trained model that can be called. Saved models are in __trained_models__ folder

    Parameters- pipeline_to_save: class sklearn.pipeline.Pipeline object                        


    Outputs-

> load_pipeline(filename):

Loads the saved pipeline from the specified path

    Parameters- filename: str                         
                Path to the file.

    Outputs- class sklearn.pipeline.Pipeline object

> remove_old_pipelines(files_to_keep)

Remove old model pipelines. Used during saving a pipeline.

    Parameters- files_to_keep: class sklearn.pipeline.Pipeline object                         
                Path to the file.

    Outputs-
