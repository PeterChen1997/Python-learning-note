# -*- coding: utf-8 -*-
# TCP编程

# 一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket

# 导入socket, threading, time库
import socket
import threading
import time


# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口
# 0.0.0.0:绑定到所有网络地址
# 127.0.0.1:外部计算机无法连接
s.bind(('0.0.0.0', 9999))

# 5表示制定等待连接的最大数量
s.listen(5)
print('Wating for connection...')

def tcplink(sock, addr):
  print('Accept new connection from %s:%s...' % addr)
  sock.send(b'Welcome!')
  while True:
    data = sock.recv(1024)
    time.sleep(1)
    if not data or data.decode('utf-8') == 'exit':
      break
    # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.send(('Received!').encode('utf-8'))
    print(data.decode('utf-8'))
  sock.close()
  print('Connection from %s:%s closed.' % addr)
  
# 通过循环接受连接
# accept()会等待并返回一个客户端的连接
while True:
  # 接受一个新连接
  sock, addr = s.accept()
  # 创建新线程来处理TCP连接
  t = threading.Thread(target = tcplink, args = (sock, addr))
  t.start()

sock.close()
s.close()