import random

class ProbabilityTableError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        print value


def select_with_probability(num, table):
    try:
        assert(sum(table.values()) == 1)
    except:
        print sum(table.values())
        raise ProbabilityTableError("Probability table does not sum to 1: %d")
    r=0
    for i in range(len(table.keys())):
        key = table.keys()[i]
        if i == len(table.keys()) - 1:
            if num < 1 and num > r:
                return key
        else:
            if num <= r + table[key] and num >= r:
                return key
        r += table[key]
    return -1

#def add_to_probability_table(s,table):


if __name__ == "__main__": 
    import doctest
    doctest.testmod()
    results = []
    results_stats = {}
    table = {
                1: 0.2,
                2: 0.3,
                3: 0.3,
                4: 0.2
            }
    for i in range(10000):
        results.append(select_with_probability(random.random(),table))
    for i in results:
        if i not in results_stats:
            results_stats[i] = 1
        else:
            results_stats[i] += 1
    print results_stats
