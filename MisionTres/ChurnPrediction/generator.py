import pandas as pd

# Crear un DataFrame con datos ficticios
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male'],
    'SeniorCitizen': [0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    'Partner': ['Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes'],
    'Dependents': ['No', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'No'],
    'Tenure': [5, 2, 8, 10, 1, 20, 15, 3, 5, 6],
    'PhoneService': ['Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No'],
    'MultipleLines': ['No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No'],
    'InternetService': ['DSL', 'DSL', 'Fiber optic', 'Fiber optic', 'DSL', 'Fiber optic', 'DSL', 'DSL', 'Fiber optic', 'Fiber optic'],
    'OnlineSecurity': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No'],
    'OnlineBackup': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes'],
    'DeviceProtection': ['No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes'],
    'TechSupport': ['No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No'],
    'StreamingTV': ['No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes'],
    'StreamingMovies': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes'],
    'Contract': ['Month-to-month', 'Two year', 'One year', 'Month-to-month', 'Two year', 'One year', 'Month-to-month', 'Month-to-month', 'Two year', 'One year'],
    'PaperlessBilling': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'PaymentMethod': ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Electronic check', 'Credit card (automatic)', 'Mailed check', 'Electronic check', 'Electronic check', 'Credit card (automatic)', 'Bank transfer (automatic)'],
    'MonthlyCharges': [29.85, 56.95, 53.85, 42.30, 70.70, 99.65, 89.10, 29.75, 104.80, 56.35],
    'TotalCharges': [188.95, 108.15, 869.45, 1840.75, 70.70, 1990.50, 1290.60, 82.95, 2250.45, 1193.65],
    'Churn': ['No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
 
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
df.to_excel('/mnt/data/churn_data.xlsx', index=False)
