#!/usr/bin/venv python3

import threading
from time import sleep, ctime


loops = [4, 2]
def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        # 实例化 Thread(调用 Thread())和调用 thread.start_new_thread() 的最大区别是新线程不会立即开始执行
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    # join()方法将等􏰘线程结束，或者在􏰉供了超时时间的 情况下，达到超时时间。使用 join()方法要
    # 比等􏰘􏲗释放的无限􏰟环更加清晰(这也是这种􏲗 又称为自旋锁􏵈􏵉􏲥的原因)。
    for i in nloops:
        # join()方法只有在需要等􏰘线程完成的时候才是有用的。
        threads[i].join() # wait for all threads to finish

    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()


