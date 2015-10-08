import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "../../"))
from PyMarkovChain import markov
import pickle

with open("anna_corpus.pickle.txt") as f:
    anna_corpus = pickle.load(f)

def gen_sentence(corpus,init=".",terminator="."):
    curr_word = corpus.select_outcome(init)
    sentence = []
    while curr_word != terminator:
        sentence.append(curr_word)
        curr_word = corpus.select_outcome(curr_word)
    print " ".join(sentence) + "."

gen_sentence(anna_corpus)
