import pandas as pd
import shap
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def calculate_shap_values(adjusted_data, cluster_labels, raw_data):
    """
    This function calculates SHAP values for each class.
    Returns shap_values and formatted_data.
    """

    # Fitting the RandomForest model
    clf = RandomForestClassifier()
    clf.fit(adjusted_data, cluster_labels)


    # Convert NumPy array to Pandas DataFrame
    adjusted_data_df = pd.DataFrame(adjusted_data, columns=raw_data.columns)

    # Calculation of SHAP values
    explainer = shap.TreeExplainer(clf)
    shap_values = explainer.shap_values(adjusted_data_df)

    return shap_values, adjusted_data_df, explainer



