pyFeel is a python library, it will facilitate your emotion analysis.
pyFeel calculates seven emotions: positivity, joy, sadness, anger, surprise, disgust.
_______________
pyFeel est une librairie en python, elle vous facilitera vos analyses d'émotions.
pyFeel calcule sept émotions : positivité, joie, tristesse, colère, surprise, dégout.

_________________




    from pyFeel import feel
    >>> test = feel("Ma classe marche bien, c'est génial non ?")
    >>> test.emotions()
    Out : {'positivity': 1.0, 'joy': 0.25, 'fear': 0.0, 'sadness': 0.25, 'angry': 0.0, 'surprise': 0.0, 'disgust': 0.0}



 For more information contact me: adilzoutinegm@gmail.com
_____________

For the lexicon : Amine Abdaoui, Jérôme Azé, Sandra Bringay et Pascal Poncelet. FEEL: French Expanded Emotion Lexicon. Language Resources and Evaluation, LRE 2016, pp 1-23.

_________

Bibliograpy :
 - Ekman, P., 1992. An argument for basic emotions. Cognition & emotion 6, 169–200.  
- Mohammad, S.M., Turney, P.D., 2013. Crowdsourcing a Word-Emotion Association Lexicon. Computational Intelligence 29, 436–465.
