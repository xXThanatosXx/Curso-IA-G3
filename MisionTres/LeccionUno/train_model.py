import tensorflow as tf
import numpy as np
import os
# Definir y entrenar la red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(3,)),
    tf.keras.layers.Dense(5, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Datos de entrenamiento
train_data = [
    ([0, 0, 0], [1]),
    ([1, 1, 1], [0]),
    ([0, 1, 0], [0]),
    ([0, 0.43, 1], [1]),
    ([1, 0, 0], [1])
]

X_train = np.array([x for x, y in train_data])
y_train = np.array([y for x, y in train_data])

# Compilar y entrenar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100, verbose=0)

# Guardar el modelo entrenado en la misma carpeta que el script
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'color_model.h5')
model.save(model_path)

print("Modelo entrenado y guardado como 'color_model.h5'")

