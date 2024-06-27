import pandas as pd
import numpy as np

# Definir el número de muestras
num_samples = 1000
num_zones = 4
samples_per_zone = num_samples // num_zones

# Generar datos aleatorios para cada parámetro de calidad de agua
np.random.seed(42)  # Para reproducibilidad

# Rango típico de cada parámetro
ph = np.random.uniform(6.0, 8.5, num_samples)
turbidez = np.random.uniform(0, 5, num_samples)  # NTU (Unidades Nefelométricas de Turbidez)
conductividad = np.random.uniform(50, 1500, num_samples)  # μS/cm (microsiemens por centímetro)
oxigeno_disuelto = np.random.uniform(5, 14, num_samples)  # mg/L (miligramos por litro)
temperatura = np.random.uniform(0, 35, num_samples)  # °C

# Crear una lista ordenada de zonas, repetidas de forma equitativa
zonas = (['norte'] * samples_per_zone +
         ['centro'] * samples_per_zone +
         ['oeste'] * samples_per_zone +
         ['sur'] * samples_per_zone)

# Si el número de muestras no es múltiplo exacto de num_zones, completar las zonas restantes
zonas.extend(['norte', 'centro', 'oeste', 'sur'][:num_samples % num_zones])

# Mezclar las zonas para distribuirlas de manera aleatoria
np.random.shuffle(zonas)

# Crear un DataFrame
data = pd.DataFrame({
    'ph': ph,
    'turbidez': turbidez,
    'conductividad': conductividad,
    'oxigeno_disuelto': oxigeno_disuelto,
    'temperatura': temperatura,
    'zona': zonas
})

# Ordenar por zona para tener el dataset organizado
data = data.sort_values(by='zona').reset_index(drop=True)

# Guardar en un archivo CSV
data.to_csv('./ChatGPT/quality_water_data.csv', index=False)

print("Dataset creado y guardado como 'quality_water_data.csv'.")

