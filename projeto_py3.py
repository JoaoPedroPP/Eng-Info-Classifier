#==============================================================================
# Arquivo do projeto utilizando Python 3
# 
# Projeto que utilizando técnicas de Processamento em Línguas Naturais (PLN, ou
# do inglês NLP - 'Natural Language Processing') classifica textos de Engenharia
# em Português da revista do IEEE da América Latina em alguma das subáreas do 
# curso de Engenharia de Informação.
# 
# Dados atuais refletem o número de termos existentes para cada subárea
# 
#
#
#==============================================================================

###################Codificacao correta dos caracteres######################
#coding: utf-8



#######################Bibliotecas nencessárias############################
import nltk
from nltk.corpus import PlaintextCorpusReader
import numpy as np
import matplotlib.pyplot as plt
import os
import termoschave
import histograma_py3
###########################################################################

######################Configuração inicial#################################

#==============================================================================
# #pyVersao = input("Você está utilizando Python 3 ou 2? ")
# 
# 

caminhopasta = os.getcwd()
caminho = os.getcwd() + '/Corpus'
os.chdir(caminho)
A = os.listdir()

t = PlaintextCorpusReader(caminho, '.*')
  

 
 #print (t.words('Texto_%d'%i))
 
texTel = np.zeros(len(A))
texEle = np.zeros(len(A))
texComp = np.zeros(len(A))
texMult = np.zeros(len(A))
texRede = np.zeros(len(A))
texTot = np.zeros(len(A))


for i in range(len(A)):
  
    print('Texto_%d'%i)
    tel = 0
    ele = 0
    com = 0
    redinfo = 0
    procmul = 0
    palavras = nltk.Text(t.words('Texto_%d'%i))


    for w in nltk.Text(t.words('Texto_%d'%i)):
        w.lower()
        
        if w in termoschave.tele(): 
            #print (w)
            tel += 1
        if w in termoschave.elec(): 
            #print (w)
            ele += 1
        if w in termoschave.comp(): 
            #print (w)
            com += 1
        if w in termoschave.redinf():
            #print (w)            
            redinfo += 1
        if w in termoschave.procmult():
            #print (w)            
            procmul += 1
   
   
    for j in range (len(palavras) -1):
        w2 = palavras[j]+' ' + palavras[j+1]
        w2.lower()
        
        if w2 in termoschave.tele(): 
            #print (w2)
            tel += 1
        if w2 in termoschave.elec(): 
            #print (w2)
            ele += 1
        if w2 in termoschave.comp(): 
            #print(w2)
            com += 1
        if w2 in termoschave.redinf():
            #print (w2)            
            redinfo += 1
        if w2 in termoschave.procmult():
            #print (w2)            
            procmul += 1
            
 

    for k in range (len(palavras) -2):
        w = palavras[k]        
        w2 = palavras[k]+' ' + palavras[k+1]
        w3 = palavras[k]+' ' + palavras[k+1] +' '+palavras[k+2]
        w.lower()
        w2.lower()
        w3.lower()
         
        if w3 in termoschave.tele():
            #print (w3)
            tel += 1
        if w3 in termoschave.elec():
            #print (w3)
            ele += 1
        if w3 in termoschave.comp():
            #print(w3)
            com += 1
        if w3 in termoschave.redinf():
            #print (w3)            
            redinfo += 1
        if w3 in termoschave.procmult():
            #print (w3)            
            procmul += 1
            
    texTel[i] = tel 
    texEle[i] = ele 
    texComp[i] = com 
    texMult[i] = procmul 
    texRede[i] = redinfo 
    texTot[i] = texTel[i] + texEle[i] + texComp[i] + texMult[i] + texRede[i]

    print ("Palavras da Telecomunicações %d"%tel)
    print ("Palavras da Eletrônica %d"%ele)
    print ("Palavras da Computação %d"%com)
    print ("Palavras de Redes de Informação %d"%redinfo)
    print ("Palavras de Processamento Multimidia %d"%procmul)
    plt.figure(i) 
    plt.title('Texto_%d'%i)
    histograma_py3.graph(tel, ele, com, redinfo, procmul)
    plt.savefig(str(caminhopasta)+'\\Histogramas/Texto_'+str(i)+'.jpg')
print ("-----FIM-----")

print (np.sum(texTot))


pTel = np.zeros(len(A))
pComp = np.zeros(len(A))
pEle = np.zeros(len(A))
pMult = np.zeros(len(A))
pRede = np.zeros(len(A))
pTot = np.zeros((len(A), 5))
pTotdebug = np.zeros((len(A), 5))

areas = ['Computação', 'Eletrônica', 'Processamento Multímidia', 'Redes de Informação', 'Telecomunicações']

for i in range(len(A)):
    pComp[i] = (texComp[i]/texTot[i])*100
    pEle[i] = (texEle[i]/texTot[i])*100
    pMult[i] = (texMult[i]/texTot[i])*100
    pRede[i] = (texRede[i]/texTot[i])*100
    pTel[i] = (texTel[i]/texTot[i])*100
    pTot[i,:] = [pComp[i], pEle[i], pMult[i], pRede[i], pTel[i]]
    pTotdebug[i,:] = [pComp[i], pEle[i], pMult[i], pRede[i], pTel[i]]
    
    if pTot[i, np.argmax(pTot[i,])] >= 70:
        print('O texto %d'%i,'é da área de: ' +areas[np.argmax(pTot[i,])]+', com %d'%pTot[i, np.argmax(pTot[i,])],'%.')
        
    else:
        pos = np.argmax(pTot[i,])
        maxi = pTot[i, pos]
        pTot[i, pos] = 0
        
        if max + pTot[i, np.argmax(pTot[i,])] >= 80:
            print('O texto %d'%i,'é das áreas de: ' +areas[pos]+' e '+areas[np.argmax(pTot[i,])] ) 
                  
        else:
            pos2 = np.argmax(pTot[i,])
            maxi2 = pTot[i, pos2]    
            pTot[i, pos2] = 0  
            if maxi + maxi2 + pTot[i, np.argmax(pTot[i,])] >= 80:
                print('O texto %d'%i,'é das áreas de: ' +areas[pos]+', '+areas[pos2]+' e '+areas[np.argmax(pTot[i,])] ) 
            else:
                print('O texto %d'%i,'não é classificável em alguma subárea em específico')


np.average(texTel)
np.average(texEle)
np.average(texComp)
np.average(texMult)
np.average(texRede)

