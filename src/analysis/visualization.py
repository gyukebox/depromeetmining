import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self):
        pass

    def __str__(self):
        return 'Visualization methods class'

    def plot_bar(self, dataset):
        data = np.array([datum[1] for datum in dataset])
        names = [datum[0] for datum in dataset]
        fig, ax = plt.subplots()
        rects1 = ax.bar(np.arange(len(data)), data)
        ax.set_xticklabels(names)
        plt.show()

    def plot_bar_pandas(self, pdframe):
        """
        Plots bar graph from given pandas DataFrame
        :param pdframe: pandas DataFrame
        :return: void. Graph will shown in GUI or Jupyter console
        """
        rc('font', family='AppleGothic')
        pdframe.plot.bar()
        plt.show()
