import sys
import pandas as pd
import shap
from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from generate_test_data import create_test_dataset
import numpy as np

'------------------------------------ Information about import export format data -------------------------------------'
'''
This module will import the test dataset or your dataset with real data.
It will also format the data according to a standard.
Finally, it will export all results and plots.
'''
'----------------------------------------------------------------------------------------------------------------------'


def import_data(source_path, test_data):
    """
    It is important to consider the format of the CSV file because if the format does not meet these requirements,
    it cannot be imported.
    The CSV file must have the following format
    One value per cell. Each column represents one dimension and each row represents one data point.
    """
    # Import your data set
    if test_data.lower() == 'no':
        try:
            raw_data = pd.read_csv(source_path, sep=';', decimal=',')
            # Delete first column with ID´s
            prepared_data = raw_data.iloc[:, 1:]

            return raw_data, prepared_data
        except FileNotFoundError:
            print(f"ERROR: File '{source_path}' not found.")
            sys.exit()

    # Import test data
    if test_data.lower() == 'yes':
        raw_data = create_test_dataset()
        # Delete first column with ID´s
        prepared_data = raw_data.iloc[:, 1:]

        return raw_data, prepared_data


def format_data(prepared_data):
    # Delete first column with ID´s
    #prepared_data = raw_data.iloc[:, 1:]

    # Create an imputation transformer
    imputer = SimpleImputer(strategy="mean")

    # Impute the missing values
    raw_data_imputer = imputer.fit_transform(prepared_data)

    # Convert the imputed NumPy array back to a DataFrame
    raw_data_imputer = pd.DataFrame(raw_data_imputer, columns=prepared_data.columns)

    # Get the column indices in the raw_data_imputer based on column_names
    raw_data_imputer_columns = raw_data_imputer.columns
    column_name = 'LT'

    # Check if the column is present in the DataFrame
    if column_name in raw_data_imputer_columns:
        # Find the index of the column with the name 'LT'
        column_index = raw_data_imputer_columns.get_loc(column_name)

        # Check if the index is found
        if column_index >= 0:
            # Get the 'LT' column and update the values
            lt_column = raw_data_imputer.iloc[:, column_index]

            # Check for zeros to avoid division by zero
            if not any(lt_column == 0):
                # Calculate the reciprocal and update the values in the 'LT' column
                raw_data_imputer[column_name] = 1 / lt_column
            else:
                print("The 'LT' column contains zeros. Avoiding division by zero.")

    # Normalize the numeric dataset
    scaler = MinMaxScaler()
    normalized_numeric_data = scaler.fit_transform(raw_data_imputer)

    return normalized_numeric_data


def export_plots(figures, save_path, cluster_method):
    """
    This function exports the generated plots to the specified directory.
    """
    valid_figures = [fig for fig in figures if fig is not None]

    if valid_figures:
        for idx, fig in enumerate(valid_figures):
            if isinstance(fig, plt.Figure):
                plot_path = save_path + f'/{cluster_method}_plot_{idx}.png'
                fig.savefig(plot_path)
                print(f"Plot {idx} was saved in the file {plot_path}")
            elif isinstance(fig, shap.plots._force.AdditiveForceVisualizer):
                # If it's an AdditiveForceVisualizer, use save_html() method
                plot_path = save_path + f'/{cluster_method}_plot_{idx}.html'
                shap.save_html(plot_path, [fig.data])
                print(f"Plot {idx} was saved in the file {plot_path}")
            else:
                print(f"Unsupported figure type: {type(fig)}")

    else:
        print("No valid figures found for export.")


def export_data_csv(raw_data, cluster_labels, save_path, cluster_method):
    if not isinstance(raw_data, pd.DataFrame):
        df = pd.DataFrame(raw_data)
    else:
        df = raw_data.copy()

    # Check the difference in the number of rows
    row_difference = len(df) - len(cluster_labels)

    if row_difference == 0:
        # If the number of rows is identical, do nothing
        # Adds the column Labels to the DataSet
        df['Labels'] = cluster_labels
        pass
    elif row_difference == 1:
        # If the difference is 1, shift 'Labels' column downwards by one position
        df_with_labels = pd.DataFrame(index=df.index[:-1])
        df_with_labels['Labels'] = cluster_labels
        df_with_labels.index += 1  # Increase the index of 'df_with_labels' by 1 to make space for an additional value
        df = pd.concat([df, df_with_labels], axis=1)
    elif row_difference == 2:
        # If the difference is 2, shift 'Labels' column downwards by two positions
        df_with_labels = pd.DataFrame(index=df.index[:-2])
        df_with_labels['Labels'] = cluster_labels
        df_with_labels.index += 2  # Increase the index of 'df_with_labels' by 1 to make space for an additional value
        df = pd.concat([df, df_with_labels], axis=1)
    else:
        # If the difference is more than 2, raise an error or handle as needed
        raise ValueError("Difference in the number of rows is greater than 2, handling not specified.")

    # Save the cluster labels as a CSV file.
    labels_path = save_path + '/' + cluster_method + '.csv'
    print("CSV with added cluster labels were saved in the file", labels_path)

    # Export the DataFrame as a CSV file
    df.to_csv(labels_path, index=False)


def export_scatter_plot(fig_scatter, save_path, cluster_method):
    if fig_scatter is not None:
        plot_path = save_path + '/' + cluster_method + '_scatter.png'
        fig_scatter.savefig(plot_path)
        print("The scatter plot was saved in the file", plot_path)


def export_dendrogram(fig_dendrogram, save_path, cluster_method):
    if fig_dendrogram is not None:
        plot_path = save_path + '/' + cluster_method + '_dendrogram.png'
        fig_dendrogram.savefig(plot_path)
        print("The dendrogram was saved in the file", plot_path)
