# 4-grams_NLP

processSentence(sentence,posLex,negLex,tagger) is the function used in code,
The parameters of this function are a sentence (a string), a set of positive words, a set of negative words, and a POS tagger. 
The function should return a list with all the 4-grams in the sentence that have the following structure:                                                   

not <any word> <pos/neg word> <noun>

For example: not a good idea

 
The 4grams returned by your function should only include words and have the exact same format as the output of the run() function of textminer.py.
For example: [('not', 'a', 'great', 'book'), ('not', 'the', 'best', 'restaurant')] etc
