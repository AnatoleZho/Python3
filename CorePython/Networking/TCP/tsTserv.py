
# 导入了 time.ctime()和 socket 模块的所有属性

from socket import *
from time import ctime


HOST = ''       # HOST 变量是空白的，这是对 bind()方法的标识，表示它可以使用任何可用的地址
PORT = 21567    # 选择了一个随机的端口号，并且该端口号似乎没有被使用或被系统保留
BZUGSIZ = 1024  # 对于该 应用程序，将缓冲区大小设置为 1KB。可以根据网络性能和程序需要改变这个容量
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM) # 分配了 TCP 服务器套接字
tcpSerSock.bind(ADDR) # 将套接字绑定到服 务器地址以及开启 TCP 监听器的调用
tcpSerSock.listen(5) # listen() 方法的参数是在连接被转接或拒绝之前，传入连接请求的最大数。

'''
# 一旦进入服务器的无限循环之中，就(被动地)等待客户端的连接。当一个连接请求出现时，进入对话循环中，
# 在该循环中等待客户端发送的消息。如果消息是空白的，这意味着客户端已经退出，所以此时将跳出对话循环，
# 关闭当前客户端连接，然后等待另一个客户端连接。如果确实得到了客户端发送的消息，就将其格式化并返回
# 相同的数据，但是会在这些数据中加上当前时间戳的前缀。最后一行永远不会执行，它只是用来提醒读者，
# 如果写了一个处理程序来考虑一个更加优雅的退出方式，正如前面讨论的，那么应该调用 close()方法
'''
while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BZUGSIZ)
        if not data:
            break
        tcpCliSock.send(('[{}] {}'.format(ctime(), data.decode())).encode())

    tcpCliSock.close()
# tcpSerSock.close()

