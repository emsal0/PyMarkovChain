import probability 
import random

class ProbabilityRow:
    
    def __init__(self,row=None):
        if row is None:
            row = {}
        self.row = row
        self.count = sum(self.row.values())
    def init_item(self,item):
        self.row[item] = 0 
    def add_one(self,item):
        if item in self.row:
            self.row[item] += 1 
        else:
            self.row[item] = 1
        self.count += 1
    def __setitem__(self,key,item):
        self.row[key] = item
    def __getitem__(self, item):
        return self.row[item]
    def __iter__(self):
        return self.row.itervalues()
    def select_with_probability(self):
        seed = random.random()
        probs = dict([(i,float(self.row[i])/self.count) for i in self.row])
        return probability.select_with_probability(seed,probs) 
    def __str__(self):
        return "ProbabilityRow("+str(self.row)+")"

class Corpus:

    def __init__(self,rows=None):
        if rows is None:
            rows = {}
        self.table = rows
    def add_new_item(self,item):
        if item in self.table:
            return
        else:
            self.table[item] = ProbabilityRow()
            for key in self.table.keys()[:]: 
                self.table[item].init_item(key)
                self.table[key].init_item(item)
            self.table[item][item] = 0
    def add_one(self,spec):
        start = spec[0]
        end = spec[1]
        self.add_new_item(start)
        self.add_new_item(end)
        self.table[start].add_one(end)
    def select_outcome(self,seed):
        return self.table[seed].select_with_probability()
    def __str__(self):
        keystrs = [str(i) for i in self.table.keys()]
        return "Corpus(" + ", ".join(keystrs) + ")"
    def __getitem__(self,item):
        return self.table[item]
    def __iter__(self):
        return self.table.iteritems()

testcorpus = Corpus()

a = [(random.randint(1,20),random.randint(1,20)) for i in range(100000)]
for i in range(len(a)):
    testcorpus.add_one(a[i])

init = 1
print testcorpus.select_outcome(init)
