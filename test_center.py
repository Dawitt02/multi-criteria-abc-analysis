import pandas as pd


from import_export_format_data import import_data, export_data_csv, format_data
from perform_scoring import *
from perform_clustering import *
from program_assistant import *


source_path = '/Users/dawittvoss/Documents/UNI/Masterarbeit/Masterarbeit_Latex/Python/Final_dataset_David_MA 2.csv'

# --- Where should the results be saved? Specify your desired path. ---
# Example: save_path = '/Users/dawittvoss/Library/Mobile Documents/com~apple~CloudDocs/David/SC2Test'
save_path = '/Users/dawittvoss/Library/Mobile Documents/com~apple~CloudDocs/Johanna & David/SC2Test'

# --- Do you want to use test data? Specify 'yes' or 'no'. ---
test_data = 'no'

# --- Do you use boolean or numeric data? Specify 'bool' or 'num'. ---
data_format = 'num'

cluster_method = 'test'

# --- Please select your available data features! Specify 'yes' or 'no'.---
selling_volume                = 'yes'
average_unit_cost             = 'yes'
stockout_cost                 = 'yes'
demand_per_anual              = 'yes'
leadtime                      = 'yes'
criticality                   = 'yes'
supplier_availibility_rate    = 'yes'
number_of_customer            = 'yes'
import seaborn as sns

raw_data, prepared_data = import_data(source_path, test_data)
formatted_data = format_data(raw_data)
data = pd.DataFrame(prepared_data)

"""
# KDE-Plot für 'average unit cost'
plt.figure(figsize=(12, 7))
sns.kdeplot(data['AUC'], shade=True, color="r", label="Average Unit Cost")
plt.title('Kernel Density Estimation (KDE) for Average Unit Cost')
plt.legend()
plt.show()

# KDE-Plot für 'Lead Time'
plt.figure(figsize=(12, 7))
sns.kdeplot(data['LT'], shade=True, color="g", label="Lead Time")
plt.title('Kernel Density Estimation (KDE) for Lead Time')
plt.legend()
plt.show()

# KDE-Plot für 'Selling volume'
plt.figure(figsize=(12, 7))
sns.kdeplot(data['Selling Volume'], shade=True, color="b", label="Selling Volume")
plt.title('Kernel Density Estimation (KDE) for Selling Volume')
plt.legend()
plt.show()

"""

plt.figure(figsize=(5, 4))  # Erstellt eine neue Figur für den Plot
plt.hist(data['LT'], bins=20, color='skyblue')
plt.xlabel('Lead Time')
plt.ylabel('Frequency')
plt.show()  # Zeigt den aktuellen Plot an und bereitet das Fenster für den nächsten Plot vor

# Histogramm für 'Lead Time'
plt.figure(figsize=(5, 4))  # Erstellt eine neue Figur für den Plot
plt.hist(data['AUC'], bins=20, color='lightgreen')
plt.xlabel('Average Unit Cost')
plt.ylabel('Frequency')
plt.show()  # Zeigt den aktuellen Plot an und bereitet das Fenster für den nächsten Plot vor

# Histogramm für 'Selling Volume'
plt.figure(figsize=(5, 4))  # Erstellt eine neue Figur für den Plot
plt.hist(data['Selling Volume'], bins=20, color='salmon')
plt.xlabel('Selling Volume')
plt.ylabel('Frequency')
plt.show()  # Zeigt den Plot an

# Histogramm für 'Selling Volume'
plt.figure(figsize=(5, 4))  # Erstellt eine neue Figur für den Plot
plt.hist(data['Criticality'], bins=20, color='salmon')
plt.xlabel('Criticality')
plt.ylabel('Frequency')
plt.show()  # Zeigt den Plot an

# Histogramm für 'Selling Volume'
plt.figure(figsize=(5, 4))  # Erstellt eine neue Figur für den Plot
plt.hist(data['Supplier availability rate'], bins=20, color='salmon')
plt.xlabel('Supplier availability rate')
plt.ylabel('Frequency')
plt.show()  # Zeigt den Plot an

# Boxplots für jedes Feature
plt.figure(figsize=(15, 5))

sns.boxplot(x=data['AUC'])
plt.title('Boxplot of Average Unit Cost')
plt.show()

sns.boxplot(x=data['LT'])
plt.title('Boxplot of Lead Time')
plt.show()

sns.boxplot(x=data['Selling Volume'])
plt.title('Boxplot of Selling Volume')
plt.show()

# Violin-Plots für jedes Feature
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.violinplot(x=data['AUC'], color='skyblue')
plt.title('Violin Plot of Average Unit Cost')

plt.subplot(1, 3, 2)
sns.violinplot(x=data['LT'], color='lightgreen')
plt.title('Violin Plot of Lead Time')

plt.subplot(1, 3, 3)
sns.violinplot(x=data['Selling Volume'], color='salmon')
plt.title('Violin Plot of Selling Volume')

plt.tight_layout()
plt.show()


"""
data = pd.DataFrame(prepared_data)
# Save the cluster labels as a text file.
labels_path = save_path + '/' + cluster_method + '.csv'
print("CSV with added cluster labels were saved in the file", labels_path)

# Exportieren Sie das DataFrame als CSV-Datei
data.to_csv(labels_path, index=False)
"""
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import label_binarize
kmeanModel = KMeans(n_clusters=3)
y=kmeanModel.fit(df).labels_
y = label_binarize(y, classes=[0,1,2])
clf=RandomForestClassifier()
clf.fit(df,y)

import shap
explainer= shap.TreeExplainer(clf)
shap_values = explainer(df).values

# Summary Plot erstellen
shap.summary_plot(shap_values, df)




# Save the cluster labels as a text file.
labels_path = save_path + '/' + cluster_method + '.csv'
print("CSV with added cluster labels were saved in the file", labels_path)

# Exportieren Sie das DataFrame als CSV-Datei
df.to_csv(labels_path, index=False)


'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

import pandas as pd
import matplotlib.pyplot as plt

# Beispiel DataFrame mit normalisierten Daten
data = {
    'Lead Time': [0.2, 0.4, 0.6, 0.8, 1.0],
    'Selling Volume': [0.1, 0.3, 0.5, 0.7, 0.9],
    'Stockout cost': [0.2, 0.4, 0.6, 0.8, 1.0]
}

df = pd.DataFrame(data)

# Definiere die Gewichtungen für die ausgewählten Parameter
weighting_factors = {'Selling Volume': 1, 'Stockout cost': 1, 'Lead Time':2}

# Multipliziere die Werte der ausgewählten Parameter mit den Gewichtungen
for feature, weight in weighting_factors.items():
    df[feature] *= weight

# Erstelle einen Scatterplot ohne PCA
plt.scatter(df['Lead Time'], df['Selling Volume'], c='blue', marker='o')

plt.title('Weighted Data')
plt.xlabel('Selling Volume')
plt.ylabel('Lead Time')
plt.legend()
plt.show()
"""