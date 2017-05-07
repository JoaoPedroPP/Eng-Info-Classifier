###################Codificacao correta dos caracteres######################
#coding: utf-8

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


#######################Bibliotecas nencessárias############################
import nltk
from nltk.corpus import PlaintextCorpusReader
import numpy as np
import os
import termoschave
#import histograma
###########################################################################

######################Configuração inicial#################################

#==============================================================================
# #pyVersao = input("Você está utilizando Python 3 ou 2? ")
# 
# 

pyVersao = '2'
  
if pyVersao == '3':
    caminho = os.getcwd() + '\\Corpus'
    os.chdir(caminho)
    A = os.listdir()
    i = 5
    t = PlaintextCorpusReader(caminho, '.*')
  
if pyVersao == '2':
    caminho = os.getcwd() + '/Corpus'
    os.chdir(caminho)
    A = os.listdir()
    i = 13
    t = PlaintextCorpusReader(caminho, '.*')
  

 
 #print (t.words('Texto_%d'%i))
 
texTel = np.zeros(len(A))
texEle = np.zeros(len(A))
texComp = np.zeros(len(A))
texMult = np.zeros(len(A))
texRede = np.zeros(len(A))


for i in range(len(A)):
#for i in range(11):    
    #print (A[i])
    print('Texto_%d'%i)
    tel = 0
    ele = 0
    com = 0
    redinfo = 0
    procmul = 0
    portuguese_stopwords = nltk.corpus.stopwords.words('portuguese')
    for w in nltk.Text(t.words('Texto_%d'%i)):
        w.lower()
        if w not in portuguese_stopwords:
            if w in termoschave.tele():
                #print w
                tel += 1
            if w in termoschave.elec():
                #print w
                ele += 1
            if w in termoschave.comp():
                #print w
                com += 1
            if w in termoschave.redinf():
                redinfo += 1
            if w in termoschave.procmult():
                procmul += 1
    #nltk.Text(t.words('Texto_%d'%i)).collocations(20)
    print ("Palavras da Telecomunicações %d"%tel)
    print ("Palavras da Eletrônica %d"%ele)
    print ("Palavras da Computação %d"%com)
    print ("Palavras de Redes de Informação %d"%redinfo)
    print ("Palavras de Processamento Multimidia %d"%procmul)
    
    texTel[i] = tel
    texEle[i] = ele
    texComp[i] = com
    texMult[i] = procmul
    texRede[i] = redinfo
    #histograma.graph(tel, ele, com, redinfo, procmul)
print ("-----FIM-----")