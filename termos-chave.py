# -*- coding: utf-8 -*-

#==============================================================================
# Código para armazenar os termos-chave de cada disciplina na sua subárea
# 
# Feito individulamente para melhor visualização do PP da UFABC
# 
#
#
#==============================================================================

#######################Computação############################
progSoftEmb = ['C', 'C++', 'orientada a objeto', 'IDE', 'debug', 'compilação', 'UML', 'software']

Computacao = progSoftEmb

###Opção limitada - Computacao###
progEstru = ['algoritmos', 'linguagens compiladas', 'compilação', 'processos', 'ponteiros', 'alocação estática', 'alocação dinâmica', 'vetores', 'matrizes', 'funções', 'registros', 'arquivos', 'recursividade']
progOrientObj =['Python', 'orientada a objeto', 'objeto', 'classe', 'instância', 'herança', 'polimorfismo', 'método', 'diagrama UML', 'fluxograma']
eSCMCritica = ['SWEBOK', 'SPIN', 'promela', 'máquinas de estados', 'validação de sistemas']
infoSoci = ['Inteligência Social', 'sistemas sociais', 'ciência de redes', 'redes virais', 'formação de opinião', 'computação social']
pLN = ['PLN', 'NLP', 'nltk', 'línguas naturais', 'língua natural', 'linguística', 'tradução automática', 'semântica']
dispMoveis = ['J2ME', 'MIDlet', 'CLDC', 'MIDP', 'GUI', 'aplicativos', 'Android', 'iOS', 'java', 'C#', ' Java', 'API', 'APIs']
jogosDigi = ['jogos', 'Unity3d', 'Unity', 'VR', 'sprite', 'sprites', 'videogame', 'jogo']
sistInt = ['rede neural', 'redes neurais', 'machine learning', 'perceptron' , 'SVM', 'rede convolucional', 'backpropagation', 'algoritmo genético', 'ADALINE', 'vetor de suporte', 'aprendizado de máquina', 'lógica fuzzy', 'Machine Learning', 'neurônio', 'neurônios']
engSoftware = ['Engenharia de Software', 'CASE', 'desenvolvimento de software', 'gerência de projeto']
algoEstruDado1 = ['estruturas lineares', 'pilhas', 'listas encadeadas', 'árvores', 'oredenação', 'strings']
sistDistribuidos = ['comunicação entre processos', 'modelo cliente servidor', 'RPC', 'sincronização', 'transação distribuída', 'P2P', 'cluster', 'cloud', 'Cloud']

Computacao = Computacao + progEstru + progOrientObj + eSCMCritica + infoSoci + dispMoveis + pLN + jogosDigi + sistInt + engSoftware + algoEstruDado1 + sistDistribuidos



#######################Eletrônica############################
circuitos1 = ['corrente', 'tensão', 'Kirchoff', 'RMS', 'circuito', 'impedância', 'resistência', 'CC', 'CA', 'potenciômetro', 'bípolo', 'potência', 'capacitância', 'Farad','indutância', 'indutor', 'resistor', 'quadripolo', 'capacitor', 'capacitores', 'indutores', 'acoplamento'] 
dispElet = ['diodo', 'transistor', 'amplificador', 'fonte de tensão', 'fonte de corrente', 'bjt', 'mosfet', 'fet', 'semicondutores', 'led', 'retificação', 'zener', 'espelho de corrente', 'eletrônica', 'transformador']
eletDigi = ['porta lógica', 'AND', 'OR', 'XOR', 'NAND', 'multiplexador', 'demultiplexador', 'flip-flop', 'DAC', 'ADC', 'booleana', 'booleano', 'contador', 'mux', 'demux', 'eletrônica digital', 'portas lógicas', 'NOT', 'ROM', 'EEPROM', 'RAM', 'FPGA', 'VHDL', 'Verilog']
sistMicro = ['microprocessador', 'registradores', 'Assembly', 'microcontrolador', 'DMA', 'ALU']

Eletronica = dispElet + circuitos1 + eletDigi + sistMicro

###Opção limitada - Eletronica###
apliMicroControl = ['computação em tempo real', 'microprocessada', '8051', 'z80', 'Arduino', 'sensor', 'sensores', 'PIC']

Eletronica = Eletronica + apliMicroControl



#######################Telecomunicações############################
transform = ['transformada de Fourier', 'sistemas lineares', 'transformada de Laplace', 'Domínio da frequência', 'convolução', 'série de Fourier','espectro' ]
princComu = ['modulação', 'AM', 'FM', 'PM', 'modulação analógica']
sinAl = ['processo estocástico', 'densidade espectral', 'bayesiano', 'Bayes', 'ruído', 'bayesiana']
pds = ['sinais digitais', 'transformada z', 'tempo discreto', 'FFT', 'transformada rápida de Fourier']
comuDigi = ['sistemas de transmissão', 'AWGN', 'ruído branco', 'filtro casado', 'codificação de gray', 'QAM', 'QPSK', 'OOK', 'm-ários', 'ASK', 'bluetooth', 'zigbee', 'BER', 'SER', 'SNR', 'CNR', 'baud-rate', 'baud', 'm-ário']
tic = ['entropia', 'codificação', 'Shannon-Fano', 'Huffman', 'Lempel-Ziv', 'codificação de canal', 'Hamming', 'detecção de erro', 'convolucionais', 'Viterbi', 'convolucional']
comMov = ['sistemas móveis', 'hand-off', 'co-canal', 'modelos de propagação', 'sem-fio', 'padrões celulares', 'GSM', 'AMPS', '3G', 'EDGE', 'interferência', 'roaming', 'broadcast', 'rádio-base', 'CDMA']
ondasEle =['propagação', 'Maxwell', 'guia metálico', 'eletromagnetismo', 'ondas', 'eletromagnéticas', 'eletromagnético', 'eletromagnética', 'onda', 'radiação', 'linhas de transmissão']
propAnt = ['propagação', 'antena', 'dipolo', 'Yagi-Uda', 'Friis', 'rádio propagação',  'antenas']

Telecomunicacoes = transform + princComu + sinAl + pds + comuDigi + tic + comMov + ondasEle + propAnt

###Opção limitada - Telecom###
simulComun = ['banda-base', 'banda-passante', 'múltiplo acesso']
sistMicroOnda = ['micro-ondas', 'microondas', 'microfita', 'parâmetros S', 'casador de impedância', 'casamento de impedância', 'ADS', 'CST', 'Wilkinson', 'coplanar', 'casadores', 'osciladores', 'divisores', 'rat-race']
projAltaFreq = ['PLL', 'transceptor', 'RF', 'transceptores', 'redes de casamento', 'osciladores', 'sintetizadores de frequência']
projSistComu = ['demodulação', 'codificação de fonte', 'diagrama de olho', 'TDM', 'FDM', 'multiplexação', 'demultiplexação', 'aliasing', 'sincronismo']

Telecomunicacoes = Telecomunicacoes + simulComun + sistMicroOnda + projAltaFreq + projSistComu



#######################Redes de Informação############################
redesComp = ['redes de computadores', 'LAN', 'MAN', 'WAN', 'TCP/IP', 'UDP', 'OSI', 'internet', 'roteamento', 'roteador', 'switch', 'protocolos', 'topologia', 'roteadores', 'switches', 'protocolo']
comoOpt = ['difração', 'fibras ópticas', 'fotodetectores', 'amplificador óptico', 'óptico', 'óptica', 'gorjeio']
telFixa = ['teoria de tráfego', 'SS7', 'ISDN', 'DSL', 'VoIP', 'NGN', 'PDH', 'SDH', 'PON', 'GPON', 'telefonia', 'telefonia fixa', 'sinalização', 'discagem', 'DTMF', 'discagem']

RedesInformacao = redesComp + comoOpt + telFixa

###Opção limitada - Redes###
redesAltaVel = ['alta velocidade', 'frame relay', 'ATM', 'MPLS', 'GMPLS', 'IP over ATM', 'banda larga', 'WDM', 'OTN', 'ASON']
teoriaFila = ['erlang', 'Poisson', 'Markov', 'G/M/1', 'M/G/1', 'G/G/1', 'filas', 'fila']
gerencIntRedes = ['TMN', 'SNMP', 'WBEM', 'CORBA', 'gerenciamento de redes']
segurInfo = ['segurança da informação', 'segurança', 'criptografia', 'criptográficos', 'DoS', 'chaves públicas', 'Firewall', 'Firewalls', 'ICP-Brasil']
infoIndus = ['SCADA', 'CLP', 'OLE', 'controlador lógico programável', 'IEC', 'OPC-DA']
tecRedeOptica = ['redes ópticas', 'WDM', 'RWA', 'comutação óptica']
planRede = ['rede de acesso', 'planejamento de redes']

RedesInformacao = RedesInformacao + redesAltaVel + teoriaFila + gerencIntRedes + segurInfo + infoIndus + tecRedeOptica + planRede



#######################Processamento Multímidia############################
comuMult = ['multimídia', 'mp3', 'jpg', 'jpeg', 'wma', 'wav', 'quantização', 'amostragem', 'imagem', 'áudio', 'wavelet', 'DWT', 'codec', 'codificação']

ProcessamentoMultimidia = comuMult

###Opção limitada - Multimidia###
filtraAdap =['filtragem adaptativa', 'Wiener', 'predição linear', 'Kalman', 'gradiente descendente', 'RLS', 'LMS']
procVideo = ['openCV', 'vídeo', 'colorimetria', 'processamento de imagem', 'processamento de imagens', 'fluxo ótico', 'deblurring', 'vídeo digital', 'teleconfêrencia', 'vídeos', 'visão computacional', 'filtro gaussiando', 'filtro de mediana']
tvDigi = ['TV', 'televisão', 'teledifusão', 'Ginga', 'PAL', 'NTSC', 'SECAM', 'ATSC', 'DVB', 'ISDB', 'Transport Stream', 'feixe de transporte']
introVozAcus = ['voz', 'acústico', 'VOCODER', 'fala', 'harmônica', 'psicoacústica', 'fonador', 'fonologia', 'espectograma', 'predição linear', 'audição', 'auditivo', 'música', 'falada', 'cantada', 'musical']
filtroDigi = ['filtros digitais', 'FIR', 'IIR', 'filtro digital']
fundProcGraf = ['openGL', 'OpenGL', 'processamento gráfico', 'iluminação', 'tonalização', 'textura', 'CG', 'computação gráfica', '3D', 'pipeline gráfico', 'GPU', 'hardware gráfico']
apliMultVoz = ['sonorização', 'eletroacústica', 'acústica', 'auditivas']
projSistMult = ['multimídia', 'manipulação de imagens', 'Watermarking', 'síntese']

ProcessamentoMultimidia = ProcessamentoMultimidia + filtraAdap + procVideo + tvDigi + introVozAcus + filtroDigi + fundProcGraf + apliMultVoz + projSistMult



###Contagem total de termos###
Total = Computacao + Eletronica + Telecomunicacoes + RedesInformacao + ProcessamentoMultimidia
print(len(Total))