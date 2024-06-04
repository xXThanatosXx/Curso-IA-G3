import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# --- Carga del dataset iris ---
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Selecciona dos clases de flores y las dos primeras características para simplificar la visualización
X = X[y != 2][:, [0, 1]]
y = y[y != 2]
y = np.where(y == 0, -1, 1)  # Cambiamos las etiquetas a -1 y 1 para ADALINE

# Escalamos las características para un mejor rendimiento de ADALINE
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

class AdalineGD:
    """
    Implementación de ADALINE.
    """
    def __init__(self, learning_rate=0.01, n_iterations=50):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        self.weights = np.zeros(1 + X.shape[1])
        self.cost = []  # <-- Almacena el coste en cada época
        
        for i in range(self.n_iterations):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)
            self.weights[1:] += self.learning_rate * X.T.dot(errors)
            self.weights[0] += self.learning_rate * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.weights[1:]) + self.weights[0]

    def activation(self, X):
        return X  # Función identidad para ADALINE

    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)

# Continúa con la función de visualización y el resto del código como en el ejemplo anterior.

adaline = AdalineGD(learning_rate=0.01, n_iterations=50)
adaline.fit(X_train, y_train)

# --- Visualización ---
plt.figure(figsize=(12, 6))

# Region de decisión
plt.subplot(1, 2, 1)
plot_decision_regions(X_test, y_test, adaline)  # La misma función de visualización sirve para ADALINE
plt.title('Region de Decisión')
plt.xlabel('Longitud del sépalo estandarizada')
plt.ylabel('Ancho del sépalo estandarizado')
plt.legend(loc='upper left')

# Coste por época
plt.subplot(1, 2, 2)
plt.plot(range(1, len(adaline.cost) + 1), adaline.cost, marker='o')
plt.title('Coste por Época')
plt.xlabel('Épocas')
plt.ylabel('Sum-squared-error')

plt.tight_layout()
plt.show()

# Evaluación usando MSE
y_pred = adaline.predict(X_test)
print('MSE: %.2f' % mean_squared_error(y_test, y_pred))
