from sys import getsizeof
import time
import threading
d={}
t_s=0
av_size=1073741824
def is_present(a):
    global t_s
    if a in d:
        if d[a][1]!=-1 and d[a][1]<time.time():
            t_s-=getsizeof(d[a])
            d[a][1]=-2
            t_s+=getsizeof(d[a])
        if d[a][1]==-2:
            return False,"Time to LIVE is Over"
        else:
            return True,d[a]
    else:
        return False,"Key does not Exist"
def create(a,b,TTL=-1):
    global t_s

    if type(a)!=str:
        return "Key is not a string"
    elif len(a)>32:
        return "Size of key string is greater than 32"
    elif getsizeof(b)>16*1024:
        return "Size of value is greater than 16 KB"
    elif a in d:
        return "Key value pair already present"
    else:
        if TTL!=-1:
            sReq = t_s+getsizeof({a:[b,TTL+time.time()]})
        else:
            sReq = t_s+getsizeof({a:[b,-1]})
        if sReq>=av_size:
            return "Memory FULL, Delete Some items"
        if TTL!=-1:
            d[a]=[b,TTL+time.time()]
        else:
            d[a]=[b,-1]
        t_s+=getsizeof(d[a])
        return "Key Created" 
        
def read(a):
    rtr,msg = is_present(a)
    if rtr:
        return msg[0]
    else:
        return msg

def delete(a):
    global t_s
    rtr,msg = is_present(a)
    if rtr:
        t_s-=getsizeof(d[a])
        del d[a]
        return "Key-Value pair Deleted"
    else:
        return msg