import matplotlib.pyplot as plt
import itertools
import numpy as np


def plot_feature_importances(model, X_train):
    n_features = X_train.shape[1]
    plt.figure(figsize=(8, 8))
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), X_train.columns.values)
    plt.xlabel('Feature importance')
    plt.ylabel('Feature')


def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion Matrix, without normalization')

    print(cm)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)
    cax = ax.matshow(cm, cmap=cmap)

    plt.title(title, fontdict={'size': 14})
    fig.colorbar(cax)
    ax.set_xticklabels([''] + classes, fontdict={'size': 14})
    ax.set_yticklabels([''] + classes, fontdict={'size': 14})
    plt.xlabel('Predicted', fontdict={'size': 14})
    plt.ylabel('True',      fontdict={'size': 14})
    plt.grid(b=None)
    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 fontdict={'size': 14, 'weight': 'heavy'},
                 color="white" if cm[i, j] > thresh else "black")
    plt.show()
