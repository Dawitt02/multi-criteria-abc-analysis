import pandas as pd
import shap
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from perform_explanation import calculate_shap_values


def convert_to_letters(adjusted_data, raw_data, cluster_labels, prepared_data, shap_values, important_criteria):
    """
    Convert cluster information and SHAP values into a list of letters based on specific conditions.

    Parameters:
    - adjusted_data: NumPy array representing the adjusted data.
    - raw_data: NumPy array representing the raw data.
    - cluster_labels: Array containing cluster labels for each data point.
    - prepared_data: DataFrame containing prepared data.

    Returns:
    - cluster_labels_mapped: List of letters corresponding to the class mappings based on SHAP values and cluster information.
    """

    # 1. Calculate the average SHAP values for each feature in each cluster
    average_shap_values = np.mean(shap_values, axis=0)


    # 2. Calculate the absolute values of SHAP values
    absolute_shap_values = np.abs(shap_values)

    # 3. Calculate the mean of the absolute SHAP values for each feature across all classes
    mean_absolute_shap_values = np.mean(absolute_shap_values, axis=(0, 1))


    # 4. Identify the column in prepared_data with the highest overall mean SHAP value
    highest_mean_shap_criterion = prepared_data.columns[np.argmax(mean_absolute_shap_values)]
    print('Following criteria has the most impact for classificatio of class A:', highest_mean_shap_criterion)


    # 5. Select the corresponding column from prepared_data
    if important_criteria == None:
        selected_column = prepared_data[highest_mean_shap_criterion]
    else:
        selected_column = prepared_data[important_criteria]


    # 5. Calculate the mean value for each class (cluster) separately
    mean_value_cluster_0 = selected_column[cluster_labels == 0].mean()
    mean_value_cluster_1 = selected_column[cluster_labels == 1].mean()
    mean_value_cluster_2 = selected_column[cluster_labels == 2].mean()

    # 6. Create a mapping of classes to letters based on the selected feature
    if highest_mean_shap_criterion == 'LT':
        class_mapping = {
            np.argmin([mean_value_cluster_0, mean_value_cluster_1, mean_value_cluster_2]): 'A',
            np.argmax([mean_value_cluster_0, mean_value_cluster_1, mean_value_cluster_2]): 'C',
            3 - np.argmin([mean_value_cluster_0, mean_value_cluster_1, mean_value_cluster_2]) - np.argmax(
                [mean_value_cluster_0, mean_value_cluster_1, mean_value_cluster_2]): 'B'
        }
    else:
        class_mapping = {
            np.argmax([mean_value_cluster_0, mean_value_cluster_1, mean_value_cluster_2]): 'A',
            np.argmin([mean_value_cluster_0, mean_value_cluster_1, mean_value_cluster_2]): 'C',
            3 - np.argmax([mean_value_cluster_0, mean_value_cluster_1, mean_value_cluster_2]) - np.argmin(
                [mean_value_cluster_0, mean_value_cluster_1, mean_value_cluster_2]): 'B'
        }

    # 7. Create the final list of letters based on the class mappings
    cluster_labels_mapped = np.array([class_mapping[label] for label in cluster_labels])

    # 8. Create the final list of letters based on the class mappings
    list_letter = [class_mapping[cluster] for cluster in range(3)]

    return cluster_labels_mapped, list_letter, highest_mean_shap_criterion





