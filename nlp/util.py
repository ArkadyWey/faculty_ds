import itertools
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix


def clean_tweet(text):
    # encode tweets as utf-8 strings
    text = text.decode("utf-8")
    # remove commas in numbers (else vectorizer will split on them)
    text = re.sub(r",([0-9])", "\\1", text)
    # sort out HMTL formatting of &
    text = re.sub(r"&amp", "and", text)
    # strip urls
    return re.sub(r"http[s]{0,1}://[^\s]*", "", text)


def plot_confusion_matrix(
    y_true,
    y_pred,
    classes=["T", "F"],
    normalize=False,
    title="Confusion matrix",
    cmap=plt.cm.Blues,
    labels=[True, False],
    axis=None,
    y_lab="Actual",
    x_lab="Predicted",
):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.

    Parameters
    ----------
    y_true : array_like
        Array of true labels.
    y_pred : array_like
        Array of predicted labels.
    classes : list(str)
        Class names used for axis labels.
    normalize : boolean, optional
        If set to true, normalize so that true label rows sum to 1.
    title : str, optional
        Title to be displayed on the plot.
    cmap : Colormap, optional
        Colormap used for colouring the confusion matrix.
    labels : list, optional
        List of labels to let user specify ordering on confusion matrix.
    axis : matplotlib.pyplot.axis, optional
        Allow user to pass axis of their own when creating subplots.

    Returns
    -------
    fig : matplotlib.pyplot.figure
        Matplotlib figure of plotted confusion matrix.
    axis : matplotlib.pyplot.axis
        Axis corresponding to the returned figure.
    """
    # compute confusion matrix and normalize if required.
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    if normalize:
        cm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]

    # if axis haven't been passed as an argument, then create new ones
    if axis is None:
        fig, axis = plt.subplots(figsize=(6, 6))
    else:
        fig = None

    axis.imshow(cm, interpolation="nearest", cmap=cmap)
    axis.set_title(title, fontsize=20)

    tick_marks = np.arange(len(classes))
    axis.set_xticks(tick_marks)
    axis.set_xticklabels(classes, fontsize=18)
    axis.set_yticks(tick_marks)
    axis.set_yticklabels(classes, fontsize=18)

    fmt = ".3f" if normalize else "d"
    thresh = cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        axis.text(
            j,
            i,
            format(cm[i, j], fmt),
            fontsize=16,
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black",
        )

    axis.set_ylabel(y_lab, fontsize=18)
    axis.set_xlabel(x_lab, fontsize=18)
    axis.grid(False)

    if fig is not None:
        plt.tight_layout(pad=3)

    return fig, axis


def evaluate_model(clf):
    """
    model: sklearn pipeline
        A trained sklearn pipeline.
    """

    test = pd.read_pickle("test_tweets.pkl")
    test["text"] = test["text"].map(clean_tweet)

    score = clf.score(test["text"], test["label"])
    preds = clf.predict(test["text"])
    print(f"Model's accuracy on holdout set is {score:.3f}")
    f, ax = plot_confusion_matrix(
        test["label"], preds, classes=["Obama", "Trump"]
    )
    return f, ax
