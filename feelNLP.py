import pandas as pd
import numpy as np
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from nltk.stem.snowball import FrenchStemmer

# Importing the dataset
dataset = pd.read_csv('FEEL1.csv')
dataset = dataset.drop(['id'], axis=1)
X = dataset.iloc[:, 1].values
Y = dataset.iloc[:, 2].values
Z = dataset.iloc[:, 3].values
P = dataset.iloc[:, 4].values
Q = dataset.iloc[:, 5].values
R = dataset.iloc[:, 6].values
S = dataset.iloc[:, 7].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X = labelencoder_X.fit_transform(X)

path = 'C:\\Users\\kiit1\\Documents\\Python\\ABI Health\\ftragedy'
arr = os.listdir(path)
n8=0
print('Id    Total Words  Positive  Negative   Joy    Fear   Sadness   Anger   Surprise   Disgust')
for i in arr:
    path1 = 'C:\\Users\\kiit1\\Documents\\Python\\ABI Health\\ftragedy\\'+i
    with open(path1, encoding="utf-8") as f:
        c = f.read()
        tokens = nltk.word_tokenize(c,language='french')
        no_commas = re.sub(r'[.|,|\']',' ', c) 
        tokens = nltk.word_tokenize(no_commas) 
        text=nltk.Text(tokens)
        stopword_list = stopwords.words('french')
        
        words=[w.lower() for w in text] 
               
        filtered_words = []
        for word in words:
            if word not in stopword_list and word.isalpha() and len(word) > 1:
                filtered_words.append(word) 
        filtered_words.sort()
        #print(filtered_words)
        
        
        stemmed_words = [] 
        stemmer = FrenchStemmer() 
        for word in filtered_words:
            stemmed_word=stemmer.stem(word) 
            stemmed_words.append(stemmed_word) 
        stemmed_words.sort() 
        #print(stemmed_words)
        total_words = len(c)
        #print(total_row)
        polarity_pos = 0
        polarity_neg = 0
        joy1 = 0
        fear1 = 0
        sadness1 = 0
        anger1 = 0
        surprise1 = 0
        disgust1 = 0
        n1=0
        n2=0
        n3=0
        n4=0
        n5=0
        n6=0
        n7=0
        
        for j in stemmed_words:
            for k in dataset['word']:
                if j == k:
                    df1=X[n1]
                    df2=Y[n2]
                    df3=Z[n3]
                    df4=P[n4]
                    df5=Q[n5]  
                    df6=R[n6]
                    df7=S[n7]    
                    if df1:
                        polarity_pos = polarity_pos+1
                    else:
                        polarity_neg = polarity_neg+1
                    if df2:
                        joy1 = joy1+1
                    if df3:
                        fear1 = fear1+1
                    if df4:
                        sadness1 = sadness1+1
                    if df5:
                        anger1 = anger1+1
                    if df6:
                        surprise1 = surprise1+1
                    if df7:
                        disgust1 = disgust1+1
                    n1= n1+1
                    n2 = n2+1
                    n3= n3+1
                    n4 = n4+1
                    n5 = n5+1
                    n6 = n6+1
                    n7= n7+1
        n8=n8+1        
        print("\n",n8,"\t",total_words,"    ",polarity_pos,"\t",polarity_neg,"\t ",joy1,"\t",fear1 ,"\t",sadness1,"\t  ",anger1,"\t  ",surprise1 ,"\t    ",disgust1) 
        f.close()
