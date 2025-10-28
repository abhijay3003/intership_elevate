from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import numpy as np

def export_tree_graph(tree, feature_names, out_path="outputs/tree.dot"):
    export_graphviz(tree, out_file=out_path, feature_names=feature_names,
                    class_names=["No Disease", "Disease"], filled=True)

def plot_feature_importance(model, feature_names, out_path="outputs/feature_importance.png"):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    plt.figure(figsize=(10,6))
    plt.title("Feature Importances")
    plt.bar(range(len(feature_names)), importances[indices], align="center")
    plt.xticks(range(len(feature_names)), [feature_names[i] for i in indices], rotation=90)
    plt.tight_layout()
    plt.savefig(out_path)