from pymarkovchain import MarkovChain

mc = MarkovChain('./markov')
mc.generateDatabase(file('data').read())

lines = file('data').read().split("\n")

for i in range(10):
    r = mc.generateString()
    if r in lines:
        continue
    print r
