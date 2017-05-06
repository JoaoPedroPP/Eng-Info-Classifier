###################Codificacao correta dos caracteres######################
#coding: utf-8

###########################################################################
#######################Bibliotecas nencessárias############################
import nltk
from nltk.corpus import PlaintextCorpusReader
import os
import termoschave
import histograma

###########################################################################
######################Configuração inicial#################################
os.chdir('/home/joaopedropp/Uptpt/')
A = os.listdir('/home/joaopedropp/Uptpt/')
textos = '/home/joaopedropp/Uptpt/'
t = PlaintextCorpusReader(textos, '.*')

###########################################################################
######################Vetores de Classificacao#############################
Tele = ["dsl", "amps", "analógico", "amplificador", "ansi", "antena", "banda", "broadband", "cdma", "comutação",
        "discagem", "dsl", "dtmf", "erlang", "espectro", "rádio-base", "frequência", "gsm", "hertz", "interferência",
        "isdn", "largura de banda", "modulação", "qpsk", "multimÍdia", "multiplexador", "pcm", "propagação", "roaming",
        "ruído", "sinalização", "tdd", "tdm", "tdma", "telefonia fixa", "canal", "viva-voz", "voip"]

Eletro = ['amperímetro', 'capacitância', 'capacitor', 'circuito', 'tensão', 'smd', 'corrente alternada',
         'corrente contínua', 'diodo', 'eletromagnetismo', 'fet', 'led', 'mosfet', 'multÍmetro', 'ohmímetro',
         'potenciômetro', 'resistividade', 'resistores', 'retificador', 'semicondutores', 'transformador',
         'transistor', 'voltímetro']

Comp = ['antivírus', 'aplicativo', 'ascii', 'backup', 'banco de dados', 'bit', 'boot', 'browser', 'bug', 'c++',
        'byte', 'cd-rom', 'compilador', 'conexão', 'cpu', 'criptografia', 'ethernet', 'ftp', 'hardware', 'hd',
        'html', 'jpg', 'keyboard', 'lan', 'monitor', 'mouse', 'desktop']

###########################################################################
####################################Main###################################
for i in range(len(A)):
    print A[i]
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
    print "Palavras da Telecomunicações %d"%tel
    print "Palavras da Eletrônica %d"%ele
    print "Palavras da Computação %d"%com
    print "Palavras de Redes de Informação %d"%redinfo
    print "Palavras de Processamento Multimidia %d"%procmul
    histograma.graph(tel, ele, com, redinfo, procmul)
    print "-----FIM-----"

###########################################################################

    #fd = nltk.FreqDist(w.lower() for w in nltk.Text(t.words('Texto_%d'%i)) if w not in portuguese_stopwords)
    #print A[i]
    #for word in fd.keys()[:20]:
        #print word, fd[word]
    #print "-----FIM-----"
    #print nltk.Text(t.words('Texto_%d'%i))
