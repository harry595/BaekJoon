def solution(inputString):
    queue=[]
    first=inputString[0]
    count=0
    success=0
    dic={'<':'>','(':')','[':']','{':'}'}
    leninputString=len(inputString)
    if(first=='}' or first==')' or first==']' or first=='>'):
        return 0
    inputString=list(inputString)
    while(inputString):
        count+=1
        i=inputString.pop(0)
        if(i=='(' or  i=='{' or  i=='[' or i=='<'):
            queue.append(i)
        if(i==')' or i=='}' or i==']' or  i=='>'):
            if(len(queue)==0):
                return -(count-1)
            else:
                tmp=queue.pop()
                if(dic[tmp]==i):
                    success+=1
                else:
                    return -(count-1)
    if len(queue) > 0:
        print(queue)
        return -leninputString+1
    else:
        return success
    