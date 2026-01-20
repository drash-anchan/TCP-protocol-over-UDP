import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",9000))
s.settimeout(2)
e=0
c=None
while True:
 d,c=s.recvfrom(1024)
 t,seq,ack,_=d.decode().split("|")
 if t=="SYN":
  s.sendto(f"SYN-ACK|0|{int(seq)+1}|".encode(),c)
 elif t=="ACK":
  break
while True:
 try:
  d,c=s.recvfrom(1024)
  t,seq,ack,p=d.decode().split("|")
  if t=="DATA":
   if int(seq)==e:
    print(p)
    e+=1
   s.sendto(f"ACK|0|{e}|".encode(),c)
  elif t=="FIN":
   s.sendto(f"FIN-ACK|0|{int(seq)+1}|".encode(),c)
   break
 except:
  pass
s.close()
