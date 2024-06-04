import numpy as np
import matplotlib.pyplot as plt

# Datos
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Compuertas lógicas
OR = np.array([0, 1, 1, 1])
AND = np.array([0, 0, 0, 1])
XOR = np.array([0, 1, 1, 0])

class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=10):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        self.weights = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iterations):
            errors = 0
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights[1:] += update * xi
                self.weights[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.weights[1:]) + self.weights[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, 0)

def plot_gate(gate, perceptron, title):
    plt.figure()
    plt.scatter(X[gate == 1][:, 0], X[gate == 1][:, 1], c='blue', marker='x', label='1')
    plt.scatter(X[gate == 0][:, 0], X[gate == 0][:, 1], c='red', marker='s', label='0')
    plt.title(title)
    
    # Region de decisión
    x_min, x_max = -0.5, 1.5
    y_min, y_max = -0.5, 1.5

    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    Z = perceptron.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.4, cmap='coolwarm')
    
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

# Entrenamiento y visualización
# OR gate
perceptron_or = Perceptron()
perceptron_or.fit(X, OR)
plot_gate(OR, perceptron_or, 'OR Gate')

# AND gate
perceptron_and = Perceptron()
perceptron_and.fit(X, AND)
plot_gate(AND, perceptron_and, 'AND Gate')

# XOR gate
perceptron_xor = Perceptron()
perceptron_xor.fit(X, XOR)
plot_gate(XOR, perceptron_xor, 'XOR Gate')
