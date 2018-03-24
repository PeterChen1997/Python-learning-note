# UDP编程
import socket,sys

# SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('0.0.0.0', 9999))

print('Bind UDP on 9999...')

# 接收数据
while True:
  # recvfrom()方法返回数据和客户端的地址与端口
  data, addr = s.recvfrom(1024)
  print('Received from %s:%s' % addr)
  print('Content: %s' % data.decode('utf-8'))
  # 用sendto()就可以把数据用UDP发给客户端
  s.sendto(b'%s' % data, addr)
  if str(data, encoding='utf-8') == 'exit':
    s.close()
    sys.exit(0)