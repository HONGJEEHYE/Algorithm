def solution(priorities, location):
    document=list(enumerate(priorities))
    answer = 0
    while True:
        cur = document.pop(0)
        result=False
        for d in document:
            # print("비교={}, {}".format(d[0], d[1]))
            if cur[1] < d[1]:
                result=True
            
        if result:
            document.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

        # print(document)
        
    
    return answer
