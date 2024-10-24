import pandas as pd

def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame or dict): The Titanic dataset as a DataFrame or a dictionary.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values = {}
    for feature in categorical_features:
        if feature in df.columns:
            unique_values[feature] = df[feature].unique()
    return unique_values
