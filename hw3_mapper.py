#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 20:44:00 2021

@author: ANDISHE
"""

#import nltk
#from nltk.corpus import stopwords
#nltk.download('stopwords')
import sys 

#dataset = open("E:\\Master_UI\\Master-3_00-01\\Adv.DataBase\\homeworks\\hw_3\\example.txt","r")

#stop_words = set(stopwords.words('english'))
#print(stop_words)
#dataset = dataset.apply(lambda x: [item for item in x if item not in stop_words])
sword=['all', 'him', 't', 're', 'mightn', 'wasn', 'll', 'between', 'other', 'shan',
       'weren', 'wouldn', 'about', 'in', "doesn't", "wouldn't", "it's", 'hers', 'have', 
       'needn', 'then', 'myself', "you'd", 'won', 'into', "weren't", 'my', 'our', 'them',
       'itself', 'against', 'to', 'again', 'further', 's', 'by', 'ourselves', "you've", 
       'yours', 'more', "didn't", 'how', 'couldn', "wasn't", 'that', 'such', 'a', 'd', 
       'same', "hasn't", 'now', "should've", 'y', "won't", 'there', 'they', 'who', 'this', 
       'few', "couldn't", 'being', 'the', 'own', 'these', 'during', 'be', 'theirs',
       'should', 'each', 'his', 'so', 'hasn', 'i', 'aren', 'mustn', 'ours', 'are', 've',
       'when', 'any', 'haven', 'those', 'because', 'where', 'once', "she's", 'am', 'an', 
       'did', 'just', 'which', 'very', 'she', 'and', 'shouldn', "don't", 'm', 'before', 
       'both', 'with', 'from', 'having', 'hadn', "you're", 'of', 'some', "mightn't",
       'yourself', 'herself', "shan't", 'o', 'or', 'for', 'why', 'yourselves', "hadn't", 
       "isn't", 'here', 'out', 'didn', 'me', 'doesn', 'has', 'than', 'whom', 'doing',
       "mustn't", 'down', 'himself', 'at', "needn't", 'only', 'over', 'he', 'as', 'while', 
       'under', 'will', "haven't", 'does', "you'll", 'were', 'you', 'nor', 'ma', 'was',
       'below', 'after', 'what', 'too', 'can', 'off', 'its', "shouldn't", 'above', 'no',
       'don', 'your', 'we', 'isn', 'themselves', 'but', 'not', 'up', 'do', 'if', 'until',
       'on', 'through', "aren't", 'ain', 'it', "that'll", 'is', 'most', 'had', 'been', 
       'her', 'their']

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    #print(words)
        
    words = [word for word in words if word.lower() not in sword]
    #print(words)
    
    for word in words:
        print("%s %s" % (word,1))
        #output.append("%s\t%s" % (word,1))
        
#print(output)
