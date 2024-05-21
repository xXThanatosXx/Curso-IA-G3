from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import cross_val_score, StratifiedKFold
import numpy as np

def evaluate_model(model, X_test, y_test, X_train, y_train):
    # Hacer predicciones
    y_pred = model.predict(X_test)
    
    # Imprimir el reporte de clasificación
    print(classification_report(y_test, y_pred))
    
    # Calcular y imprimir la AUC-ROC
    y_pred_prob = model.predict_proba(X_test)[:, 1]
    auc_roc = roc_auc_score(y_test, y_pred_prob)
    print(f"AUC-ROC: {auc_roc:.2f}")
    
    # Validación cruzada con accuracy para evitar problemas con AUC-ROC
    cv = StratifiedKFold(n_splits=3)  # Reducción a 3 pliegues
    scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='accuracy')
    print(f'Cross-Validation Accuracy scores: {scores}')
    print(f'Mean Accuracy: {np.mean(scores):.2f} ± {np.std(scores):.2f}')
