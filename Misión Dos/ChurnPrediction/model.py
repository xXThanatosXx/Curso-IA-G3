from sklearn.ensemble import RandomForestClassifier

def build_and_train_model(X_train, y_train):
    # Crear un modelo de RandomForest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Entrenar el modelo
    model.fit(X_train, y_train)
    
    return model
