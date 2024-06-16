from import_export_format_data import *

'--------------------------------- Information about program assistant -----------------------------------------------'
'''
This module will check the parameters you have entered and give you some assistance if anything is missing/incorrect.
This module also displays general information about your dataset and the operations you have selected.
'''
'----------------------------------------------------------------------------------------------------------------------'


def check_conditions(source_path, cluster_method, save_path, test_data):
    if source_path is None and test_data == 'no':
        print('ERROR: No source path for real data is set. Please go back to "source_path"')
        sys.exit()
    if test_data != 'yes' and test_data != 'no':
        print('ERROR: Please choose what kind of data you want to use. Go back to "test_data" ')
        sys.exit()
    if save_path is None:
        print('ERROR: Please choose a path where your results can be stored')
        sys.exit()
    if cluster_method is None:
        print('Please select a cluster_method. Go back to "cluster_method"')
        sys.exit()


def display_overview(source_path, cluster_method, save_path, formatted_data):
    if source_path is None:
        return print('No source path for real data is set')
    else:
        print('')
        print('We take your csv file form the path:', source_path)

    print('We will store your data under following path:', save_path)
    print('')

    print('You have selected the --', cluster_method, '-- clustering algorithm')
    print('')

    print('Data shape: ')
    print('Number of Samples: ', formatted_data.shape[0])
    print('Number of Dimensions: ', formatted_data.shape[1])
    print('')
