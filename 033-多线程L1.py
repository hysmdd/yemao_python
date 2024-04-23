# 多线程案例1
import threading
import time


def singing(name, delay):
    print(f"{name}开始唱歌")
    time.sleep(delay)
    print(f"{name}结束唱歌")


def dancing(name, delay):
    print(f"{name}开始跳舞")
    time.sleep(delay)
    print(f"{name}结束跳舞")


def single_thread():
    singing("曾可妮", 2)
    dancing("蔡徐坤", 3)


def multi_thread():
    task = []
    th1 = threading.Thread(target=singing, args=('曾可妮', 2))
    th1.start()
    task.append(th1)
    for i in range(3):
        th2 = threading.Thread(target=dancing, args=('蔡徐坤', 3))
        th2.start()
        task.append(th2)
    th1.join()
    for t in task:
        t.join()


if __name__ == "__main__":
    start_time = time.time()
    # single_thread()
    multi_thread()
    # print(threading.enumerate())
    end_time = time.time()
    print(f"\n总共消耗{end_time - start_time}秒\n")
