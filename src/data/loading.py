import config.config as cg
import pandas as pd



def load_data():
    return pd.read_csv(cg.DATA_PATH)