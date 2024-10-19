import pandas as pd

def get_numerical_df(df, numerical_features):
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame or dict): The Titanic dataset as a DataFrame or dictionary.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    # If input is a dictionary, convert it to a DataFrame
    if isinstance(df, dict):
        df = pd.DataFrame(df)

    return df[numerical_features]
