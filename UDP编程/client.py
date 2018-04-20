# -*- coding: utf-8 -*-
# UDP编程
import socket,sys,re

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 接受多个服务器
print('请输入要连接的外部服务器IP(若无则输入no)')
second_ip = input()
if second_ip != 'no':
  print('请输入要连接外部服务器端口')
  second_port = input()

while True:
  data = input()
  # 发送数据
  s.sendto(data.encode('utf-8'), ('0.0.0.0', 9999))
  if second_ip != 'no':
    s.sendto(data.encode('utf-8'), (second_ip, int(second_port)))
  # 接收数据
  info = s.recv(1024).decode('utf-8')
  # print(info)
  if 'exit' == info:
      sys.exit(0)
      s.close()
s.close()
