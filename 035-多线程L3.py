# 多线程共享全局变量
import threading

a = 0
lock = threading.Lock()


def add_num(num):
    global a
    lock.acquire()
    for i in range(num):
        a += 1
    lock.release()
    print(f"a的值是 {a}")


def main():
    for i in range(10):
        th = threading.Thread(target=add_num, args=(1000000,))
        th.start()


if __name__ == '__main__':
    main()
