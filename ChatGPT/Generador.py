import pandas as pd

# Definimos las propiedades de los materiales
materials = ['Granito', 'Mármol', 'Pizarra', 'PVC', 'Polietileno', 'Policarbonato']
properties = {
    'Dureza': [7, 5, 6, 3, 2, 3],
    'Resistencia_Compresion (MPa)': [200, 120, 90, 50, 30, 70],
    'Peso (kg/m3)': [2700, 2700, 2800, 1400, 950, 1200],
    'Costo ($/m2)': [50, 80, 40, 30, 20, 60],
    'Impacto_Ambiental (kg CO2/m2)': [20, 30, 25, 10, 5, 15],
    'Durabilidad (años)': [50, 30, 40, 20, 15, 25],
    'Estetica': [8, 10, 6, 5, 4, 7]
}

# Creamos el dataframe
df = pd.DataFrame(properties, index=materials).reset_index()
df.rename(columns={'index': 'Material'}, inplace=True)

# Guardar el dataset como un archivo .csv
file_path = 'materiales_construccion.csv'
df.to_csv(file_path, index=False)

print(f'Dataset guardado en {file_path}')
