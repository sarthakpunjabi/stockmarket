# Importing libraries:

import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')


def mymodel(testdf):
    df = pd.read_csv('stockmarket/stockapp/df.csv')
    print(testdf)
    df = df.dropna(thresh=2)
    print("Dataset shape: ", df.shape)
    df = df.drop_duplicates(subset=['text'], keep='last')
    print("Dataset shape: ", df.shape)
    df.text = df.text.astype(str)

    X_train = df['text']
    y_train = df['label']
    X_test = testdf['text']
    
    vectoriser = TfidfVectorizer(ngram_range=(1,1), max_features=500000)
    vectoriser.fit(X_train)
    print('No. of feature_words: ', len(vectoriser.get_feature_names()))

    
    X_train = vectoriser.transform(X_train)
    X_test  = vectoriser.transform(X_test)

    
    model_params = {
        
        'MultinomialNB' :{
            'model' : MultinomialNB(),
            'params' : {
                'alpha' : np.linspace(0.5, 1.5, 2, 3, 6), 'fit_prior' : [True, False]
            }
        },
    }    
    

    for model_name, mp in model_params.items():
        clf = GridSearchCV(mp['model'], mp['params'], cv=5, n_jobs=-1, verbose=1) # Using Cross Validation of 5 and n_jobs=-1 for fast training by using all the processors
        print(mp['model'])
        print('\nFitting...')
        best_model = clf.fit(X_train, y_train)                      # Training the model
        clf_pred = best_model.predict(X_test)                       # Predicting the results
    
        print('\nScore is appended.\n')

        my_arr = clf_pred
        return my_arr

    