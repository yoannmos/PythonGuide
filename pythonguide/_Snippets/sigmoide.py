# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:18:00 2019

@author: ymosteiro
"""
import numpy as np
import matplotlib.pyplot as plt


class sigmoide:
    """ Sigmoide function """

    def __init__(
        self,
        time=list(),
        time_gen=[0, 100, 101],
        tilt=1,
        inflexion_point=50,
        max_val=550,
        signe=-1,
    ):
        self.time = time
        self.time_gen = time_gen
        self.tilt = tilt
        self.inflexion_point = inflexion_point
        self.max_val = max_val
        self.signe = signe

        self.define_time_array()

    def define_time_array(self):
        """ Create time """
        if not self.time:
            self.time = np.linspace(
                self.time_gen[0], self.time_gen[1], self.time_gen[2]
            )

    # def sigmoide(time=None, inclinaison=1, pointInflexion=50, tempsMax=150, pMax=550):

    # #    if not t.any():
    # t = np.linspace(0, tempsMax, tempsMax)

    # fonc = (1 - 1 / (1 + np.exp(-inclinaison * (t - pointInflexion)))) * pMax
    # return fonc


if __name__ == "__main__":

    x = np.linspace(0, 150, 150)
    sig = sigmoide()

    print(sig.time)
    # fig = plt.figure()
    # ax = plt.axes()
    # plt.grid()
    # ax.plot(x, y)
    # plt.title("Sigmoide du Power Supply")
    # ax = ax.set(xlabel="Temps (s)", ylabel="Puissance en W ou J/s")
    # plt.show()

