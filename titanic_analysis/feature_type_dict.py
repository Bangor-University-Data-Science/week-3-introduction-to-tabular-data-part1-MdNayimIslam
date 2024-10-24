import pandas as pd

def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame or dict): The Titanic dataset as a DataFrame or dictionary.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """

    feature_types = {
        'numerical': {
            'continuous': [],  # Continuous numerical features
            'discrete': []  # Discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Nominal categorical features
            'ordinal': []  # Ordinal categorical features
        }
    }

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            if len(df[column].unique()) > 10:  # Arbitrary cutoff for continuous
                feature_types['numerical']['continuous'].append(column)
            else:
                feature_types['numerical']['discrete'].append(column)
        else:
            feature_types['categorical']['nominal'].append(column)

    return feature_types
