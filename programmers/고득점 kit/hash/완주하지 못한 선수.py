import collections

def solution(participant, completion):
    left = collections.Counter(participant) - collections.Counter(completion)
    return list(left.keys())[0]


# 중요 point
# 1. collection 모듈과 Counter
# 2. Counter(participant) - Counter(completion)
# 3. dict keys() : dict(left)의 key를 return
# 4. list(dict.keys())[0] : dict(left)의 key를 list로 변환
