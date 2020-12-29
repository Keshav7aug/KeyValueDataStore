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
    sReq = t_s+getsizeof({a:b})
    if sReq>=av_size:
        print("Memory FULL, Delete Some items")
    if type(a)!=str:
        print("Key is not a string")
    elif len(a)>32:
        print("Size of key string is greater than 16 KB")
    elif a in d:
        print("Key value pair already present")
    else:
        if TTL!=-1:
            d[a]=[b,TTL+time.time()]
        else:
            d[a]=[b,-1]
        t_s+=getsizeof(d[a])
        print("Key Created")
        
def read(a):
    rtr,msg = is_present(a)
    if rtr:
        print(msg[0])
    else:
        print(msg)

def delete(a):
    global t_s
    rtr,msg = is_present(a)
    if rtr:
        t_s-=getsizeof(d[a])
        del d[a]
        print("Deleted Key")
    else:
        print(msg)