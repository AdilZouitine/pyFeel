#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 21:51:51 2018

@author: Adil Zouitine <adilzouitinegm@gmail.com
"""
import numpy as np
from nltk import word_tokenize
import os.path


__all__ = ['feel']

class feel():
    '''
    Calculates the emotion of a string with a'bag of word' method.
    object.dict to see the bag of word.

    >>> from pyFeel import feel
    >>> test = feel("Ma classe marche bien, c'est génial non ?")
    >>> test.emotions()
    Out : {'positivity': 1.0, 'joy': 0.25, 'fear': 0.0, 'sadness': 0.25,
          'angry': 0.0, 'surprise': 0.0, 'disgust': 0.0}
    '''

    def __init__(self,text):
        '''
        Input : string Output : /
        '''

        scriptpath = os.path.dirname(__file__)
        dict_name = os.path.join(scriptpath, 'feel.npy')

        self.dict = np.load(dict_name).item()
        self.token = [word for word in word_tokenize(text.lower())]
        self.sentiment = {}
        self.number_emotion = 7
        self.vector = np.zeros(self.number_emotion)
        self.list_emotions = ['positivity',
                              'joy',
                              'fear',
                              'sadness',
                              'angry',
                              'surprise',
                              'disgust']


    def emotions(self):
        '''
        Calculates emotion by averaging the emotion vectors of each word in
        the input string and the bag of word.

        Input : (self) Output : dict
        '''
        
        retain_word = 0
        for word in self.token:
            if word.lower() in self.dict:
                self.vector = np.add(self.vector,
                                     self.dict[word],
                                     out = self.vector)
                retain_word += 1
        if retain_word != 0:
            self.vector /= retain_word
        for emotion,emotion_value in zip(self.list_emotions,self.vector):
            self.sentiment.update({emotion : float(emotion_value)})
        return self.sentiment

if __name__ == '__main__':
    test = feel("Ma classe marche bien, c'est génial non ?")
    print(test.emotions())
