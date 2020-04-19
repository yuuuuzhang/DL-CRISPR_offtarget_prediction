import numpy as np
import pandas as pd
import csv
import tensorflow as tf
from keras.models import load_model

def onehot_en(x):
    alphabet = ('A','C','G','T')
    onehotseq = np.zeros((4,20))
    for i in range(20):
        n = alphabet.index(x[i])
        onehotseq[n][i] = 1
    return onehotseq

def find_mismatch_single(a, b):
    ntarr = ("AC","AG","AT","CA","CG","CT","GA","GC","GT","TA","TC","TG")
    mismatchseq = np.zeros((12,20))
    #idx = [i for i in range(20) if a[i] != b[i]]
    #l = len(idx)

    for j in range(20):
        if a[j] != b[j]:
            char2 = a[j]+b[j]
            idx1 = ntarr.index(char2)
            mismatchseq[idx1][j] = 1
    return mismatchseq

def find_mismatch(lis1,lis2):
    feature = []
    for i in range(len(lis1)):
        seq1 = onehot_en(lis1[i]) # on
        seq2 = onehot_en(lis2[i]) # off
        seq3 = find_mismatch_single(lis1[i],lis2[i]) # mismatch
        temp = np.concatenate((seq1,seq2,seq3),axis=0)
        feature.append(temp)
    feature = np.array(feature)
    return feature

def find_mismatch_augment(lis1,lis2):
    feature0 = []
    feature1 = []
    feature2 = []
    feature3 = []
    for i in range(len(lis1)):
        seq1 = onehot_en(lis1[i]) # on
        seq2 = onehot_en(lis2[i]) # off
        seq3 = find_mismatch_single(lis1[i],lis2[i]) # mismatch
        temp = np.concatenate((seq1,seq2,seq3),axis=0)
        temp90 = np.rot90(temp)
        temp180 = np.rot90(temp,2)
        temp270 = np.rot90(temp,3)
        feature0.append(temp)
        feature1.append(temp90)
        feature2.append(temp180)
        feature3.append(temp270)
    feature0 = np.array(feature0)
    feature1 = np.array(feature1)
    feature2 = np.array(feature2)
    feature3 = np.array(feature3)
    return feature0,feature1,feature2,feature3

def off_target_pred(datapath, inputfile, outputname):
    df = pd.read_csv(inputfile,delimiter = ',')
    rawteston = df.ontarget
    rawtestoff = df.offtarget
    fea = find_mismatch(rawteston,rawtestoff)
    data_test = fea.reshape(len(fea),20,20,1) 
    print ("begin testing")
    model_name = ['m0.h5','m1.h5','m2.h5','m3.h5','m4.h5','m5.h5','m6.h5','m7.h5','m8.h5','m9.h5']
    
    probas = np.zeros((len(data_test),2))
    modelpath = datapath+'model/'

    for filename in model_name:
        model = load_model(modelpath+filename)   
        pre_rst = model.predict(data_test)
        probas = probas + pre_rst
        print ("finish model")
    probas = probas/10
    
    pred_label = []
    for i in range(len(probas)):
        if (probas[i][0]>=0.5):
            pred_label.append('off-target')
        else:
            pred_label.append('no-editting')
        
    with open(datapath+'output/'+outputname, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(list(probas[:,0]),pred_label))
            
    return