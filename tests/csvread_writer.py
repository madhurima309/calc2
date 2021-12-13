import pandas as pd

def csv_read(input_file):
    df = pd.read_csv(input_file)
    return df

def csv_writer(input_df):
    input_df.to_csv('tests/output_csv_file/output2.csv', mode='a', index=False, header=False)


