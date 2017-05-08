#==============================================================================
#
# Código com a parte de geração do histograma para melhor visualização
# 
#==============================================================================

# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def graph(tele, elec, comp, redinfo, procmult):
    totComputacao = comp
    totEletronica = elec
    totMultimidia = procmult
    totRedes = redinfo
    totTelecom = tele

    areas = ['Computação', 'Eletrônica', 'Multimídia', 'Redes', 'Telecom']
    frequencias = [totComputacao, totEletronica, totMultimidia, totRedes, totTelecom]
    xlabel = ['Computação: %d'%totComputacao, 'Eletrônica: %d'%totEletronica, 'Multimídia: %d'%totMultimidia, 'Redes: %d'%totRedes, 'Telecom: %d'%totTelecom]

    pos = np.arange(len(areas))
    width = 0.20

    ax = plt.axes()
    ax.set_xticks(pos + (width / 2) - 0.1)
    ax.set_xticklabels(xlabel)


    plt.bar(pos, frequencias, width, color='g')

plt.show()