import math
def solution(progresses, speeds):
    answer = []
    answer_ = []
    
    for i in range(len(progresses)):
        answer_.append( math.ceil((100 - progresses[i]) / speeds[i]))
    
    print(answer_)
    
    i:int = 0
    
    while i < len(answer_):
        nCount:int = 1
        j:int = i + 1
        while j < len(answer_):
            if answer_[j] <= answer_[i]:
                nCount += 1
                print(nCount)
            else:
                break
            j += 1
        i += nCount
        answer.append(nCount)        
    
    return answer