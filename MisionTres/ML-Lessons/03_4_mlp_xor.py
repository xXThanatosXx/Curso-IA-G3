import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

# Datos
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])  # XOR

# Entrenando un MLP
mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=10000, activation='tanh', solver='adam', random_state=42)
mlp.fit(X, y)

def plot_decision_regions(X, y, classifier, resolution=0.02):
    # Configurar el marcador y el mapa de colores
    markers = ('s', 'x')
    colors = ('red', 'blue')
    cmap = plt.cm.coolwarm

    # Establecer el rango para la región de decisión
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    
    # Dibuja muestras
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.8, 
                    c=colors[idx],
                    marker=markers[idx], 
                    label=cl, 
                    edgecolor='black')
        
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

# Visualizando regiones de decisión
plot_decision_regions(X, y, classifier=mlp)
