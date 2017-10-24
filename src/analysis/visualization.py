import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self):
        pass

    def __str__(self):
        return 'Visualization methods class'

    @staticmethod
    def plot_bar(dataset):
        """
        Plots bar graph from given dataset(dictionary)
        :param dataset: Dictionary-formatted data
        :return: void. Graph will shown in GUI or Jupyter console
        """
        data = np.array([datum[1] for datum in dataset])
        names = [datum[0] for datum in dataset]
        fig, ax = plt.subplots()
        _ = ax.bar(np.arange(len(data)), data)
        ax.set_xticklabels(names)
        plt.show()

    @staticmethod
    def plot_bar_pandas(pdframe):
        """
        Plots bar graph from given pandas DataFrame
        :param pdframe: pandas DataFrame
        :return: void. Graph will shown in GUI or Jupyter console
        """

        # 한글이 안 깨진다!
        rc('font', family='AppleGothic')
        ax = pdframe.plot.bar()

        # labeling data
        bar = ax.patches
        labels = [row[1] for row in pdframe.itertuples()]
        for bar, label in zip(bar, labels):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + 3, label, ha='center', va='bottom')

        plt.show()
