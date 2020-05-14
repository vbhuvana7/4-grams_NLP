#!/usr/bin/env python
# coding: utf-8
# we have used Tweet tokenizer instead of word_tokenize to avoid splitting words with apostrophe for example -let's
#Give input sentence at line 48

""" team2  -----Saroja Kondamudi,Bhuvana Vellanki,Ishan Desai ------"""

import nltk,re
from nltk.tokenize import sent_tokenize
from nltk import load
from nltk.tokenize import TweetTokenizer


def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

def processSentence(sentence,posLex,negLex,tagger):
    sentence=sentence.lower().strip()

    fourgram=[]
    tknzr = TweetTokenizer()
    terms = tknzr.tokenize(sentence)   
    tagged_terms=tagger.tag(terms)
    
    for i in range(len(tagged_terms)-3):
        term1=tagged_terms[i]
        term2=tagged_terms[i+1]
        term3=tagged_terms[i+2]
        term4=tagged_terms[i+3]
    
        if term1[0]== 'not' and term2[1] != '.' and (term3[0] in posLex or term3[0] in negLex) and re.match('NN',term4[1]) : 
            fourgram.append((term1[0],term2[0],term3[0],term4[0]))
    
    return fourgram

if __name__=='__main__':
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    posLex=loadLexicon("positive-words.txt")
    negLex=loadLexicon("negative-words.txt")
    sentence= " " # Give the input sentence here
    print(processSentence(sentence,posLex,negLex,tagger))



