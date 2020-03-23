#!/usr/bin/venv python3

import _thread

from time import sleep, ctime

loops = [4, 2]
def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release()


def main():
    print('starting at:', ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire() # 通过 acquire()方法取得(每个􏲗)。 取得􏲗效果相当于“把􏲗􏲗上”
        locks.append(lock)

    '''
    # 我们不在上锁􏲗的循􏰟环中􏰝启动线程呢?这有两个原因:
    # 其一，我们想要同步线程，以便“所有的马同时冲出围􏳶”;
    # 其二，获取锁􏲗需要花费一点时间。如果线程执行得太快，有可能出现获取􏲗之前线程就执行结束的情况
    '''
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    '''
    # 最后一个􏰟环只是坐在那里等􏰘(􏱩 􏰡主线程)，直到所有􏲗都被释放之后才会继续执行。
    # 因为我们按照顺序检查每个􏲗，所有可 能会被排在􏰟环列表前面但是执行较􏳮的􏰟环所􏳷􏳸。
    # 这种情况下，大部分时间是在等􏰘最 前面的􏰟环。当这种线程的􏲗被释放时，剩下的􏲗可能􏳲已被释放
    # (也就是说，对应的线程 已经执行完􏳹)。结果就是主线程会􏳺快地、没有􏰡􏳻地完成对剩下􏲗的检查
    '''
    for i in nloops:
        while locks[i].locked(): pass

    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()




