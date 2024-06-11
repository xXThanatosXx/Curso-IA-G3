import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Cargar el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocesar los datos
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# Usar una imagen de prueba
image_index = 0
image = test_images[image_index].reshape(1, 28, 28, 1)

# Definir el modelo de la red neuronal (mismo que el ejemplo anterior)
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Compilar y cargar los pesos entrenados del modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Crear un nuevo modelo que devuelva las salidas de las capas intermedias
layer_outputs = [layer.output for layer in model.layers]
activation_model = models.Model(inputs=model.input, outputs=layer_outputs)

# Obtener las activaciones
activations = activation_model.predict(image)

# Función para graficar las activaciones
def display_activation(activations, col_size, row_size, layer_number):
    activation = activations[layer_number]
    activation_index = 0
    fig, ax = plt.subplots(row_size, col_size, figsize=(12, 12))
    for row in range(row_size):
        for col in range(col_size):
            ax[row][col].imshow(activation[0, :, :, activation_index], cmap='viridis')
            activation_index += 1
    plt.show()

# Graficar las activaciones de la primera capa de convolución
display_activation(activations, col_size=4, row_size=8, layer_number=0)
