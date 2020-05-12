from fmi import FMI
from api import config
from datetime import date, datetime

def get_forecast():
    f = FMI(place=config.PREDICTION_PLACE)
    forecast = f.forecast()
    #make it into a dataframe
    df = pd.DataFrame()
    for i,observation in enumerate(forecast):
        df_temp = pd.DataFrame(observation.__dict__, index=np.arange(i,i+1))
        df = pd.concat([df,df_temp], axis=0)

    #get the global radiation to proper values
    df[config.GLOBAL_RADIATION] = df[config.RADIATION_ACCUMULATION].diff()/3600
    # discard first row
    df = df.loc[1:]
