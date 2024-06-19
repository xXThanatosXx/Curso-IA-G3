import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import pandas as pd
import os

# Configuración
num_samples = 1000
image_size = (64, 64)
output_dir = 'dataset'

# Crear directorios si no existen
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image_dir = os.path.join(output_dir, 'images')
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Función para generar imágenes sintéticas de plantas
def generate_plant_image(size):
    img = Image.new('RGB', size, color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Dibujar una planta simple como un conjunto de líneas
    plant_color = (34, 139, 34)  # Verde
    draw.line((size[0]//2, size[1], size[0]//2, size[1]//2), fill=plant_color, width=3)
    draw.line((size[0]//2, size[1]//2, size[0]//3, size[1]//3), fill=plant_color, width=3)
    draw.line((size[0]//2, size[1]//2, 2*size[0]//3, size[1]//3), fill=plant_color, width=3)
    
    return img

# Generar dataset
data = []
for i in range(num_samples):
    # Generar imagen
    img = generate_plant_image(image_size)
    img_path = os.path.join(image_dir, f'plant_{i}.png')
    img.save(img_path)
    
    # Generar datos sensoriales sintéticos
    temperature = np.random.uniform(18, 30)  # Celsius
    humidity = np.random.uniform(40, 70)  # Porcentaje
    ph = np.random.uniform(5.5, 6.5)
    nutrients = np.random.uniform(100, 1000)  # ppm
    
    data.append([img_path, temperature, humidity, ph, nutrients])

# Crear un DataFrame y guardar en un archivo CSV
df = pd.DataFrame(data, columns=['image_path', 'temperature', 'humidity', 'ph', 'nutrients'])
df.to_csv(os.path.join(output_dir, 'sensor_data.csv'), index=False)

print(f'Dataset generado con {num_samples} muestras.')
