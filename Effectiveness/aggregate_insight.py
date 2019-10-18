import rbo_func as rbo

def rboresult(groundtruth, new, p):
    return rbo.rbo(groundtruth, new, p)['ext']

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))
