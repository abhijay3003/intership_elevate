from src.preprocess import load_and_preprocess
from src.train_tree import train_decision_tree
from src.train_forest import train_random_forest
from src.evaluate import cross_validate_model
from src.visualize import export_tree_graph, plot_feature_importance

X, y, X_train, X_test, y_train, y_test = load_and_preprocess()

tree, tree_acc = train_decision_tree(X_train, y_train, X_test, y_test)
forest, forest_acc = train_random_forest(X_train, y_train, X_test, y_test)

print("Decision Tree Accuracy:", tree_acc)
print("Random Forest Accuracy:", forest_acc)

print("Tree CV Accuracy:", cross_validate_model(tree, X, y))
print("Forest CV Accuracy:", cross_validate_model(forest, X, y))

export_tree_graph(tree, feature_names=X.columns)
plot_feature_importance(forest, feature_names=X.columns)