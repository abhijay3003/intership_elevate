from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_random_forest(X_train, y_train, X_test, y_test, n_estimators=100):
    forest = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    forest.fit(X_train, y_train)
    y_pred = forest.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return forest, acc