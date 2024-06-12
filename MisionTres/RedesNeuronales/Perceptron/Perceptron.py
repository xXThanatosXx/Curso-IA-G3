import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar el dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

X = X[y != 2][:, [0, 1]]
y = y[y != 2]

# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Estandarizar las características
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Modificar la tasa de aprendizaje
learning_rate = 0.01  # Ajusta este valor según tus necesidades

# Entrenar el Perceptrón y registrar los errores por época

ppn = Perceptron(max_iter=1, eta0=learning_rate, random_state=42, warm_start=True)
errors = []

for _ in range(50):
    ppn.fit(X_train_std, y_train)
    y_train_pred = ppn.predict(X_train_std)
    errors.append((y_train != y_train_pred).sum())

# Realizar predicciones
y_pred = ppn.predict(X_test_std)

# Evaluar el rendimiento del modelo
print(f'Accuracy: {accuracy_score(y_test, y_pred):.2f}')

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)

# Graficar la matriz de confusión
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Setosa', 'Versicolor'], yticklabels=['Setosa', 'Versicolor'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Graficar el error por época de entrenamiento
plt.figure(figsize=(8, 6))
plt.plot(range(1, 51), errors, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of updates')
plt.title('Training Error per Epoch')
plt.show()
