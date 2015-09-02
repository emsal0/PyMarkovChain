import markov
import pickle
import time

def get_bare(word):
    puncts = [',','.']
    if word[-1] in puncts:
        return word[:-1]
    return word

with open("anna_karenina") as f:
    wordlist = f.read().replace("\n"," ").split(" ")

wordlist = filter(lambda a: a != "", wordlist)

anna_corpus = markov.Corpus()
i=0
time.sleep(1)
while i < len(wordlist) - 1:
    curr_word = wordlist[i]
    next_word = wordlist[i+1]
    i += 1
    if curr_word[0] in ["\""]:
        t = curr_word[0]
        curr_word = curr_word[1:]
        if len(curr_word) == 0:
            continue
        anna_corpus.add_one((t,get_bare(curr_word)))
    if curr_word[-1] == ',' or curr_word[-1] == '.':
        anna_corpus.add_one((curr_word[:-1],curr_word[-1]))
        curr_word = curr_word[-1]
    if next_word[0] in ["\""]:
        next_word=next_word[0]
    anna_corpus.add_one((curr_word,get_bare(next_word)))

with open("anna_corpus.pickle.txt","w") as f:
    pickle.dump(anna_corpus,f)
