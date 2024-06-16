from perform_abc_order import convert_to_letters
from perform_explanation import *
from perform_weighting import *
from perform_scoring import *
from apply_global_constraints import *
from perform_clustering import *
from program_assistant import *
from visualize_data import visualize_global_explanation, visualize_local_explanation, analyze_cluster_labels
from import_export_format_data import *

'--------------------------------- General Information ----------------------------------------------------------------'
'''

The file is structured in such a way that you can set all the parameters necessary for the functionality in
the main window.
Moreover, the structure is such that the program can be extended with the desired algorithms/scores. 
In order to get the program running, you have to set the following parameters and run this module:

IMPORTANT: In order for the program to run, the HEADER of the CSV file must be formatted accordingly.

1st column 
ID's
 
2nd to 10th column 
Feature names: 'Selling Volume', 'AUC', 'Stockout cost', 'Margin per unit', 'LT, 
'Criticality', 'Supplier availbility rate'.

'''

'--------------------------------- Set your parameters ----------------------------------------------------------------'

# --- Read data from the CSV file. Specify the path to the data.---
# Example: source_path = '/Users/dawittvoss/Library/Mobile Documents/com~apple~CloudDocs/David/SC2Test/rawdata_test.csv'
source_path = '/Users/dawittvoss/Documents/UNI/Masterarbeit/Masterarbeit_Latex/Python/Final_dataset_David_MA 2.csv'

# --- Where should the results be saved? Specify your desired path. ---
# Example: save_path = '/Users/dawittvoss/Library/Mobile Documents/com~apple~CloudDocs/David/SC2Test'
save_path = '/Users/dawittvoss/Library/Mobile Documents/com~apple~CloudDocs/Johanna & David/SC2Test'

#--- Set your focus for the classification. 0.001(99,99% resilient) -- 1 (balanced) -- 1000(99,99% cost)
adjustment_factor = 1

#--- Set global constraints for non-compensation. ----
# If selling volume < x, then the relevance of the item will be reduced by 50%
selling_volume_threshold = 0
# If average unit cost < x, then the relevance of the item will be reduced by 50%
AUC_threshold = 0
# If stockout cost < x, then the relevance of the item will be reduced by 50%
stockout_cost_threshold = 0
# If profit per unit < x, then the relevance of the item will be reduced by 50%
profit_per_unit_threshold = 0
# If Lead Time > x, then the relevance of the item will be reduced by 50%
lead_time_threshold = 2000
# If criticality < x, then the relevance of the item will be reduced by 50%
criticality_threshold = 0.99
# If supplier availability rate < x, then the relevance of the item will be reduced by 50%
supplier_availability_rate_threshold = 0

# ---- Please select one clustering method. ----

#cluster_method = 'gmm'
#cluster_method = 'kmeans'
cluster_method = 'kmedoids'

'--------------------------------------------Now you are all set-------------------------------------------------------'
# Define global constraints
global_constraints = [
    ('Selling Volume', '<', selling_volume_threshold, 0.5),
    ('AUC', '<', AUC_threshold, 0.5),
    ('Stockout cost', '<', stockout_cost_threshold, 0.5),
    ('Margin per Unit', '<', profit_per_unit_threshold, 0.5),
    ('LT', '>', lead_time_threshold, 0.5),
    ('Criticality', '<', criticality_threshold, 0.5),
    ('Supplier availability rate', '<', supplier_availability_rate_threshold, 0.3)
]

test_data = 'no'

#-- what is your most important criteria in this analysis? None if there is no
important_criteria = None

# Check, if conditions for execution are valid
check_conditions(source_path, cluster_method, save_path, test_data)

# Import raw data/test data
raw_data, prepared_data = import_data(source_path, test_data)

# Set global constraints
adjusted_data = apply_global_constraints(prepared_data, global_constraints)

# Import raw data/test data
raw_data, prepared_data = import_data(source_path, test_data)

# Format the data.
formatted_data = format_data(adjusted_data)


# Call the function to adjust the specified columns
columns_to_adjust = ['Selling Volume', 'AUC', 'Stockout cost', 'Margin per Unit', 'LT', 'Criticality', 'Supplier availability rate']
adjusted_data_2 = adjust_columns(formatted_data, raw_data, columns_to_adjust, adjustment_factor)

# General information about your Execution
display_overview(source_path, cluster_method, save_path, formatted_data)


# Perform clustering.
cluster_labels, cluster_labels_letter, list_letter, highest_mean_shap_value, class_a_indices,shap_values, \
    adjusted_data_df, explainer = perform_clustering(adjusted_data_2, cluster_method, raw_data, save_path,
                                                     adjusted_data, prepared_data, important_criteria)

# Perform calculation of scores
calculate_scores(prepared_data, cluster_labels)

# Perform Explanation.
#shap_values, adjusted_data_df, explainer = calculate_shap_values(adjusted_data, cluster_labels, prepared_data)

# Global explanation
visualize_global_explanation(shap_values, adjusted_data_df, explainer, list_letter)

#Lokal Explanation
data = pd.DataFrame(prepared_data)

mean_values_data = data.mean().round(2)
print('Mean Value AUC =', mean_values_data[1])
print('Mean Value Lead Time =', mean_values_data[0])
print('Mean Value Selling volume =', mean_values_data[2])
print('Mean Value Supplier availability rate =', mean_values_data[3])
print('Mean Value Criticality =', mean_values_data[4])

visualize_local_explanation(adjusted_data, cluster_labels, prepared_data, prepared_data, list_letter, class_a_indices, shap_values, explainer)


#figures = visualize_shap_plots(shap_values, adjusted_data_df, explainer)
# Export Plot of Explanation
#export_plots(figures, save_path, cluster_method)
