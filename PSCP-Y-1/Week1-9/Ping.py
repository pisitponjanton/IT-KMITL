"""Ping"""
def time(x):
    """time"""
    t=""
    time1 = ""
    for i in x[::-1]:
        if i == "i":
            break
        if i in ("=","<"):
            t=""
        if i == "m":
            t+=i
        elif t=="m":
            time1+=i
    if not time1:
        time1=""
    else:
        time1 = int(time1[::-1])
    return time1
def received(x):
    "Received"
    n = 0
    t = ""
    for i in x:
        t+=i
        if t == "Rep":
            n = 1
    return n
def ping():
    """Ping"""
    n1 = input()
    n2 = input()
    n2 = n1
    n1 = n2
    n3 = input()
    n4 = input()
    n5 = input()
    n6 = input()
    n7 = input()
    t = ""
    ip = ""
    for i in n3:
        if i == "]":
            t=""
        if i == "[" :
            t+=i
        elif t == "[":
            ip+=i
    if not ip:
        for i in n3[::-1]:
            if i == "g":
                t=""
            if i == "w" :
                t+=i
            elif t == "w":
                ip+=i
        ip = (ip[1:-1])[::-1]
    timem = [time(n4),time(n5),time(n6),time(n7)]
    r = received(n4) + received(n5) + received(n6) + received(n7)
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = {r}, Lost = {4-r} ({int(((4-r)/4)*100)}% loss),")
    if r>0:
        maxtime = max(v for v in timem if isinstance(v, int))
        mintime = min(v for v in timem if isinstance(v, int))
        averagetime = sum(v for v in timem if isinstance(v, int))//r
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {mintime if mintime > 1 else 0}ms, "
            f"Maximum = {maxtime if maxtime > 1 else 0}ms, "
            f"Average = {averagetime if averagetime > 1 else 0}ms")

ping()
