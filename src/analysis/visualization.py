import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self):
        pass

    def __str__(self):
        return 'Visualization methods class'

    def plot_bar(self, dataset):
        pass

    def plot_bar_pandas(self, pdframe):
        """
        Plots bar graph from given pandas DataFrame
        :param pdframe: pandas DataFrame
        :return: void. Graph will shown in GUI or Jupyter console
        """
        pdframe.plot()

