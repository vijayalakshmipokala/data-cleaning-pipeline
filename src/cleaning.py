import pandas as pd

def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
    return df

def remove_duplicates(df):
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"Removed {before - after} duplicate rows")
    return df

def fix_postal_code(df):
    df['postal_code'] = df['postal_code'].astype(str)
    return df