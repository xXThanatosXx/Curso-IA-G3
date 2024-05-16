import tensorflow as tf
import os

# Cargar el modelo entrenado desde la misma carpeta que el script
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'color_model.h5')
model = tf.keras.models.load_model(model_path)

def predict_color(rojo, verde, azul):
    prediction = model.predict([[rojo, verde, azul]])
    return 'blanco' if prediction[0][0] > 0.5 else 'negro'

# Ejemplo de uso de la función de predicción
if __name__ == "__main__":
    r, g, b = 0, 0, 0
    color = predict_color(r, g, b)
    print(f"Para RGB({r}, {g}, {b}), el color de texto debería ser {color}.")

