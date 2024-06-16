
'--------------------------------- Information about apply global constraints -----------------------------------------------'
'''
Purpose of the Module:
The "apply_global_constraints" module is designed to apply global constraints to the provided data. It expects
 formatted data in the form of a DataFrame and a list of global constraints specified as tuples.
'''
'----------------------------------------------------------------------------------------------------------------------'


def apply_global_constraints(prepared_data, global_constraints):
    '''
    Apply global constraints to the formatted data based on specified conditions.

    :param prepared_data: DataFrame, input data with columns to be constrained
    :param global_constraints: List of tuples, each containing (column_name, operator, threshold, reduction_factor)
    :return: DataFrame, data after applying global constraints
    '''

    # List to store information about adjusted rows
    adjusted_rows = []

    adjusted_data = prepared_data

    # Iterate over global constraints
    for constraint in global_constraints:
        column_name, operator, threshold, reduction_factor = constraint

        # Check if the column name is in the data
        if column_name in adjusted_data.columns:

            # Check if a value in the column exceeds or falls below the threshold
            if operator == '>':
                mask = adjusted_data[column_name] > threshold
            elif operator == '<':
                mask = adjusted_data[column_name] < threshold
            else:
                print("Unsupported operator.")
                continue

            # If yes, apply the reduction factor to the affected rows
            if any(mask):
                adjusted_rows.extend(adjusted_data.loc[mask].index)
                adjusted_data.loc[mask, :] *= reduction_factor

    # Output the information about adjusted rows
    if adjusted_rows:
        print("Adjusted rows:", adjusted_rows)
    else:
        print("No rows were adjusted.")

    return adjusted_data


