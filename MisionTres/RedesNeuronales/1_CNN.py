import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Cargar el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocesar los datos
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

train_labels = tf.keras.utils.to_categorical(train_labels, 10)
test_labels = tf.keras.utils.to_categorical(test_labels, 10)

# Usar una imagen de prueba
image_index = 0
image = test_images[image_index].reshape(1, 28, 28, 1)

# Definir el modelo de la red neuronal
model = models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilar y cargar los pesos entrenados del modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.1)

# Evaluar el modelo
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f"Precisión en el conjunto de prueba: {test_accuracy}")

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
            if activation_index < activation.shape[-1]:
                ax[row][col].imshow(activation[0, :, :, activation_index], cmap='viridis')
                activation_index += 1
    plt.show()

# Graficar las activaciones de la primera capa de convolución
display_activation(activations, col_size=4, row_size=8, layer_number=0)
