"""Using permutations from the stl"""
from itertools import permutations

characters = ['c', 'a', 't', 'd', 'o', 'g']
permutations = permutations(characters)

for perm in permutations:
    string = ''.join(perm)
    print(string)

"""Using custom implementation of permutations"""
def permutations(elements):
    if len(elements) <= 1:
        yield elements
    for perm in permutations(elements[1:]):
        for i in range(len(elements)):
            yield perm[:i] + elements[0:1] + perm[i:]


for i in permutations('catdog'):
    print(i)