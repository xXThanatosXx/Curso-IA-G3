import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Configuración
image_size = (64, 64)
num_classes = 2  # Ejemplo de clasificación binaria
batch_size = 32
epochs = 10

# Cargar el dataset (asegúrate de subir el archivo 'Iris.csv' a tu entorno de Google Colab)
from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Iris.csv')

# Cargar el dataset
data_dir = image_dir = os.path.join(data, 'images')
csv_file = os.path.join(data_dir, 'D:\Shadow\GitHub\Curso-IA-G3\dataset\sensor_data.csv')

df = pd.read_csv(csv_file)

# Función para cargar y preprocesar imágenes
def load_and_preprocess_image(image_path, size):
    img = load_img(image_path, target_size=size)
    img_array = img_to_array(img)
    img_array = img_array.astype('float32') / 255.0
    return img_array

# Cargar imágenes y datos sensoriales
X_images = np.array([load_and_preprocess_image(os.path.join(image_dir, path), image_size) for path in df['image_path']])
y_labels = np.random.randint(0, num_classes, size=(len(df)))  # Etiquetas aleatorias para clasificación binaria

# Convertir etiquetas a formato categórico
y_labels = to_categorical(y_labels, num_classes)

# Dividir el dataset en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_images, y_labels, test_size=0.2, random_state=42)

# Construcción del modelo CNN
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(image_size[0], image_size[1], 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Compilación del modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenamiento del modelo
model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.1)

# Evaluación del modelo
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_test_classes = np.argmax(y_test, axis=1)

# Calcular precisión y F1 score
accuracy = accuracy_score(y_test_classes, y_pred_classes)
f1 = f1_score(y_test_classes, y_pred_classes, average='weighted')

print(f'Accuracy: {accuracy}')
print(f'F1 Score: {f1}')
