import markov
import pickle

with open("anna_corpus.pickle.txt") as f:
    anna_corpus = pickle.load(f)

def gen_sentence(corpus,init=".",terminator="."):
    curr_word = corpus.select_outcome(init)
    while curr_word != terminator:
        print curr_word
        curr_word = corpus.select_outcome(curr_word)

gen_sentence(anna_corpus)
