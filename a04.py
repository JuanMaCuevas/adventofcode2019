import collections
increasing = lambda x: x==''.join(sorted(x))
grouped = lambda x: 2 in collections.Counter(x).values()
valid = lambda x: increasing(x) and grouped(x)

ran = range(183564,657474)
candidates = sum(1 for pas in ran if valid(str(pas)))
print(candidates)
