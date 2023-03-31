import pandas as pd

def import_data(table_name):
    "Import data from csv file."
    df = pd.read_csv(table_name)
    return df

