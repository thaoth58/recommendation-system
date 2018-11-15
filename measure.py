from math import*
from decimal import Decimal

#Jaccard similatiry
def jaccard_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/union_cardinality

#Euclidean distance
def euclidean_distance(x, y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

#Manhattan distance
def manhattan_distance(x, y):
    return sum(abs(a-b) for a,b in zip(x,y))

#Minkowski distance
def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)

def minkowski_distance(x, y, p_value):
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

#Cosine similarity
def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x, y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)

print(jaccard_similarity([0,1,2,5,6],[0,2,3,5,7,9]))
print(euclidean_distance([0,3,4,5],[7,6,3,-1]))
print(manhattan_distance([10,20,10],[10,20,20]))
print(minkowski_distance([0,3,4,5],[7,6,3,-1],3))
print(cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15]))
