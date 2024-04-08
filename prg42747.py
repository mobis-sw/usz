def solution(citations):
    answer = 0
    lst_cnt = []
    max_cnt = max(citations)
    for h in range(max_cnt, -1, -1):
        top = 0
        bottom = 0
        for cnt in citations:
            if cnt >= h:
                top += 1
            if cnt < h:
                bottom += 1
        
        if h <= top:
            answer = h
            return answer
