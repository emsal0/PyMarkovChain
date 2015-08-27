import probability

class ProbabilityRow:
    
    def __init__(self,row={}):
        self.row = row
        self.count = sum(self.table.values())
    def init_item(self,item):
        self.row[item] = 0 
    def add_one(item):
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

class Corpus:

    def __init__(self,rows={}):
        self.table = rows
    def add_new_item(self,item):
        if item in self.table:
            return
        else:
            self.table[item] = ProbabilityRow()
            for key in self.table[:]:
                self.table[item].init_item(key)
                self.table[key].init_item(item)
    def add_one(spec):
        start = spec[0]
        end = spec[1]
        self.add_new_item(start)
        self.add_new_item(end)
        self.table[start][end] = 1


# a = ProbabilityTable()
# a.add_one("asdf")
