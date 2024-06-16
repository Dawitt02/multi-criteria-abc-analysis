
# Data Processing and Analysis Suite

A suite of Python scripts for data processing, analysis, and applying constraints.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
    - [perform_abc_order.py](#perform_abc_orderpy)
    - [program_assistant.py](#program_assistantpy)
    - [test_center.py](#test_centerpy)
    - [main.py](#mainpy)
    - [import_export_format_data.py](#import_export_format_datapy)
    - [perform_explanation.py](#perform_explanationpy)
    - [apply_global_constraints.py](#apply_global_constraintspy)
4. [Contributing](#contributing)
5. [License](#license)

## Overview

This project contains a collection of Python scripts designed to perform various data processing and analysis tasks, including applying global constraints to data. Each script serves a specific purpose and can be used independently or as part of a larger workflow.

The main script (`main.py`) allows you to set all necessary parameters for functionality in the main window. The program can be extended with desired algorithms/scores, and requires specific formatting of the CSV file header for proper operation.

**CSV File Format Requirements:**
- 1st column: IDs
- 2nd to 10th columns: Feature names ('Selling Volume', 'AUC', 'Stockout cost', 'Margin per unit', 'LT', 'Criticality', 'Supplier availability rate').

## Installation

1. Clone the repository:
    \`\`\`sh
    git clone https://github.com/yourusername/your-repo-name.git
    \`\`\`
2. Navigate to the project directory:
    \`\`\`sh
    cd your-repo-name
    \`\`\`
3. (Optional) Create and activate a virtual environment:
    \`\`\`sh
    python -m venv venv
    source venv/bin/activate  # On Windows use \`venv\Scripts\activate\`
    \`\`\`
4. Install the required packages:
    \`\`\`sh
    pip install -r requirements.txt
    \`\`\`

## Usage

### perform_abc_order.py

This script is used to perform ABC analysis on given data by converting it into alphabetical categories.

**Example Usage:**
\`\`\`sh
python perform_abc_order.py
\`\`\`

**Functions:**
- \`convert_to_letters\`: Converts numerical data into corresponding alphabetical categories.

### program_assistant.py

This script serves as a program assistant for various utility functions, assisting in data processing and analysis.

**Example Usage:**
\`\`\`sh
python program_assistant.py
\`\`\`

**Functions:**
- Various helper functions to assist with the main workflow.

### test_center.py

This script is used to run test cases and validate the functionality of other scripts, ensuring the integrity and correctness of the operations.

**Example Usage:**
\`\`\`sh
python test_center.py
\`\`\`

**Functions:**
- \`run_tests\`: Executes a series of predefined tests.

### main.py

This script is the main entry point for executing the data processing and analysis workflow. It integrates multiple modules to perform comprehensive data analysis.

**Example Usage:**
\`\`\`sh
python main.py
\`\`\`

**General Workflow:**
1. Import raw data.
2. Format the data.
3. Apply global constraints.
4. Adjust specified columns.
5. Perform clustering.
6. Calculate scores.
7. Provide global and local explanations.
8. Visualize results.

**Parameters:**
- \`source_path\`: Path to the CSV data file.
- \`save_path\`: Path to save the results.
- \`adjustment_factor\`: Factor for adjusting the classification focus.
- \`global_constraints\`: List of global constraints to apply.

### import_export_format_data.py

This script handles the import and export of data, ensuring the correct format is maintained.

**Example Usage:**
\`\`\`sh
python import_export_format_data.py
\`\`\`

**Functions:**
- \`import_data\`: Imports raw data from a specified path.
- \`format_data\`: Formats the imported data for analysis.

### perform_explanation.py

This script provides explanations and detailed analysis of the processed data, using various techniques to elucidate results.

**Example Usage:**
\`\`\`sh
python perform_explanation.py
\`\`\`

**Functions:**
- \`explain_results\`: Generates detailed explanations for the data analysis results.

### apply_global_constraints.py

This script applies global constraints to the provided data based on specified conditions, modifying data that exceeds or falls below certain thresholds.

**Example Usage:**
\`\`\`sh
python apply_global_constraints.py
\`\`\`

**Functions:**
- \`apply_global_constraints\`: Applies global constraints to data based on specified conditions.

## Contributing

1. Fork the repository.
2. Create a new branch (\`git checkout -b feature-branch\`).
3. Commit your changes (\`git commit -m 'Add some feature'\`).
4. Push to the branch (\`git push origin feature-branch\`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
