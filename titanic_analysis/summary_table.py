import pandas as pd

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame or dict): The Titanic dataset as a DataFrame or dictionary.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    return pd.DataFrame({
        'Feature Name': df.columns,
        'Data Type': df.dtypes,
        'Number of Unique Values': df.nunique(),
        'Has Missing Values?': df.isnull().any()
    })
