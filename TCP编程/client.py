# -*- coding: utf-8 -*-
# TCP编程

# 导入socket库
import socket

# 创建一个socket
# AF_INET制定使用IPv4协议
# SOCK_STREAM制定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('0.0.0.0', 9999))

# 接受数据
print(s.recv(1024).decode('utf-8'))

# 发送数据
while True:
  data = input()
  s.send(data.encode('utf-8'))
  print(s.recv(1024).decode('utf-8'))
s.send(b'exit')

# 关闭连接
s.close()