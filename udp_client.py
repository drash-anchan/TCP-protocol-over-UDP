import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.settimeout(2)
s.sendto(f"SYN|0|0|".encode(),("127.0.0.1",9000))
while True:
 d,_=s.recvfrom(1024)
 t,seq,ack,_=d.decode().split("|")
 if t=="SYN-ACK":
  s.sendto(f"ACK|{ack}|{int(seq)+1}|".encode(),("127.0.0.1",9000))
  break
msgs=["Hello","This","Is","UDP-TCP"]
seq=0
for m in msgs:
 while True:
  s.sendto(f"DATA|{seq}|0|{m}".encode(),("127.0.0.1",9000))
  try:
   d,_=s.recvfrom(1024)
   t,_,ack,_=d.decode().split("|")
   if t=="ACK" and int(ack)==seq+1:
    seq+=1
    break
  except:
   print("resend")
s.sendto(f"FIN|{seq}|0|".encode(),("127.0.0.1",9000))
d,_=s.recvfrom(1024)
print("done")
s.close()
