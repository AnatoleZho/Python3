
# 从 socket 模块导入所有属性
from socket import *

'''
# HOST 和 PORT 变量指服务器的主机名与端口号。因为在同一台计算机上运行测试(在本例中)，所以 
# HOST 包含本地主机名(如果你的服务器运行在另一台主机上，那么需要进行相应修改)。端口号 PORT 
# 应该与你为服务器设置的完全相同(否则，将无法进行通信)。 此外，也将缓冲区大小设置为 1KB
'''
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 分配了 TCP 客户端套接字(tcpCliSock)，接着主动调用并连接到服务器。
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

'''
# 客户端也有一个无限循环，但这并不意味着它会像服务器的循环一样永远运行下去。客户端循环在以下
# 两种条件下将会跳出:用户没有输入或者服务器终止且对 recv() 方法的调用失败。否则，在正常情况下，
# 用户输入一些字符串数据，把这些数据发送到服务器进行处理。然后，客户端接收到加了时间戳的字符串，
# 并显示在屏幕上。
'''
while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()