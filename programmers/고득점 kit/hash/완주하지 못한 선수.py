import collections

def solution(participant, completion):
    left = collections.Counter(participant) - collections.Counter(completion)
    return list(left.keys())[0]
