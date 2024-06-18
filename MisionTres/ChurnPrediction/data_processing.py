import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def preprocess_data(data):
    # Suponiendo que la columna 'Churn' es la variable objetivo
    X = data.drop('Churn', axis=1)
    y = data['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
  

    
    # Convertir variables categóricas a variables dummy
    X = pd.get_dummies(X)
    print(X)
    # Contar el número de muestras en la clase minoritaria
    class_counts = y.value_counts()
    minority_class_count = class_counts.min()
    
    # Ajustar el número de vecinos para SMOTE
    k_neighbors = min(5, minority_class_count - 1)  # al menos 1 muestra para el vecino
    
    # Sobremuestreo de la clase minoritaria
    smote = SMOTE(random_state=42, k_neighbors=k_neighbors)
    X_res, y_res = smote.fit_resample(X, y)
    
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)
    
    # Estandarizar las características
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test
