# UDP编程
import socket,sys,re

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
  data = input()
  # 发送数据
  s.sendto(data.encode('utf-8'), ('0.0.0.0', 9999))
  # 接收数据
  info = s.recv(1024).decode('utf-8')
  # print(info)
  if 'exit' == info:
      sys.exit(0)
      s.close()
s.close()