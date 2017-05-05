# -*- coding: utf-8 -*-

#==============================================================================
# Código com a parte de geração do histograma para melhor visualização
# 
# Dados atuais refletem o número de termos existentes para cada subárea
# 
#
#
#==============================================================================

import numpy as np
import matplotlib.pyplot as plt

totComputacao = 104
totEletronica = 75
totMultimidia = 86
totRedes = 83
totTelecom = 119

areas = ['Computação', 'Eletrônica', 'Multímidia', 'Redes', 'Telecom']
frequencias = [totComputacao, totEletronica, totMultimidia, totRedes, totTelecom]

pos = np.arange(len(areas))
width = 1.0     

ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(areas)

plt.bar(pos, frequencias, width, color='g')

plt.show()