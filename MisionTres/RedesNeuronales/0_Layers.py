import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, LSTM, BatchNormalization

model = Sequential()

# Capa convolucional y de pooling
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Capa de normalización por lotes
model.add(BatchNormalization())

# Otra capa convolucional y de pooling
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Aplanar las características para conectarlas a capas densas
model.add(Flatten())

# Capas densas
model.add(Dense(units=128, activation='relu'))

# Capa de dropout
model.add(Dropout(rate=0.5))

# Capa de salida para clasificación multiclase
model.add(Dense(units=10, activation='softmax'))

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Resumen del modelo
model.summary()


