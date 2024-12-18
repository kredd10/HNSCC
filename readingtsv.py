import pandas as pd

# Replace 'your_file.tsv' with the path to your TSV file
file_path = r'C:\Users\manir\Desktop\genomic data collection\data\hnsc_tcga_clinical_data.tsv'


# Read the TSV file using pandas
df = pd.read_csv(file_path, sep='\t')

# Display the first few rows of the DataFrame
print(df.head())

# Optional: you can perform operations on the DataFrame as needed
# For example, displaying all column names
print(df.columns)

tumor_free_patients = df[df['Person Neoplasm Status'] == 'TUMOR FREE']
print(tumor_free_patients)
