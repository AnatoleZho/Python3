#!/usr/bin/venv python3

import _thread

from time import sleep, ctime

def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())

def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())

def main():
    print('starting at:', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    '''
    # 如果没有阻止主程序继续执行，它将会继续执行下一语句，显示 all DONE
    # 然后退出，而loop0() 和 loop1() 这两个线程直接终止
    # 没有写让主线程等待子线程全部完成之后再继续执行代码，即线程需要某种形式的同步。
    # 再这个例子中， 调用 sleep() 来作为同步机制
    '''
    sleep(6)
    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()
