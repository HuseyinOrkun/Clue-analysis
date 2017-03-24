#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:57:46 2017

@author: huseyin
"""
import re
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.parse.generate import generate,demo_grammar
from nltk import CFG
import nltk
from nltk.tag import pos_tag
from nltk.parse.api import ParserI

def word_tokenize(sentence):
    return nltk.word_tokenize(sentence)

def lemmatize(word, pos='n'):
    return nltk.stem.WordNetLemmatizer().lemmatize(word, pos)


def clue_preprocess(clue, answer_length):
    
    clue_type = ''
    
    processed_clue = clue

    if "_" in clue:
        clue_type = 'fill-in-the-blanks'
        under_score_no = clue.count('_')
        for i in range(under_score_no):
            if i< answer_length:
                processed_clue = processed_clue.replace("_","?")
            else:
                processed_clue = processed_clue.replace("_",None)
    else:
         print(demo_grammar)
         tokenized_word = word_tokenize(clue)   
         POS = pos_tag(tokenized_word)
         text = nltk.Text(tokenized_word)
         a = text.common_contexts(words = tokenized_word)
         print(a)
         for word,tag in POS:
             print(word, '->', tag)
             
        
    return (clue_type, answer_length,processed_clue )
"""
         parser = ParserI()
         grammar = CFG.fromstring(demo_grammar)
         print(grammar)
         parse_tree = parser.parse_sents(list(tokenized_word))
         print(type(parse_tree))
         grammar = parser.grammar()
         #print(grammar)
         for sentence in generate(parse_tree, n=10):
             print(' '.join(sentence))
    """         
    
            
            
            
x = clue_preprocess("This is a rock band", 4)
print(x)