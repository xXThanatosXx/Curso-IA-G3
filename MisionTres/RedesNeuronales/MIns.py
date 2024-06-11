import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

# Cargar el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Función para mostrar algunas imágenes del conjunto de datos
def show_images(images, labels, num_images):
    plt.figure(figsize=(10, 10))
    for i in range(num_images):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap=plt.cm.binary)
        plt.xlabel(labels[i])
    plt.show()

# Mostrar 25 imágenes del conjunto de datos de entrenamiento
show_images(train_images, train_labels, 50)
