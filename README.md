
# pyFeel

pyFeel is a python library, it will make your emotion analysis in french easier.
pyFeel computes seven emotions: positivity, joy, fear, sadness, anger, surprise, disgust
with a bag of word method.


# Installation


If you want to install it :

**Requirements**
 - Python 3
 - numpy : run `pip install numpy`
 - nltk : run `pip install nltk`
 - Don't forget to download nltk data [punkt] !!


**Let's play now !**

 - pyFeel : run `pip install git+https://github.com/AdilZouitine/pyFeel --upgrade`

**PyPI**

PyPI is coming ...
_______________

    >>> from pyFeel import Feel
    >>> test = Feel("Ma classe fonctionne bien, c'est sympathique non ?")
    >>> test.emotions()
    Out : {'positivity': 1.0, 'joy': 0.3333333333333333, 'fear': 0.0, 'sadness': 0.0, 'angry': 0.0, 'surprise': 0.0, 'disgust': 0.0}




 For more information contact me: adilzouitinegm@gmail.com

## For the lexicon

 Amine Abdaoui, Jérôme Azé, Sandra Bringay et Pascal Poncelet. FEEL: French Expanded Emotion Lexicon. Language Resources and Evaluation, LRE 2016, pp 1-23.


## Bibliograpy

 - Ekman, P., 1992. An argument for basic emotions. Cognition & emotion 6, 169–200.  
- Mohammad, S.M., Turney, P.D., 2013. Crowdsourcing a Word-Emotion Association Lexicon. Computational Intelligence 29, 436–465.
