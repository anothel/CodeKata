from sys import stdout;

def solution(record):
    answer = []
    answer_ = []
    
    d = {}
    
    
    for s in record:
        action: str = ""
        sid: str = ""
        nick: str = ""
        
        if s[:5] == "Leave":
            action, sid = map(str, s.split(" "))
            answer_.append(str(sid + "l"))
            #stdout.write("%s\n" % answer_)
        else:
            action, sid, nick = map(str, s.split(" "))
            d[sid] = nick
            if s[:5] == "Enter":
                answer_.append(str(sid + "e"))
                #stdout.write("%s\n" % answer_)
                
    for i in answer_:
        if i[-1] == "e":
            answer.append("%s님이 들어왔습니다." % d[i[:-1]])
        else:
            answer.append("%s님이 나갔습니다." % d[i[:-1]])
    
    #stdout.write("%s\n" % answer)
    
    
    return answer