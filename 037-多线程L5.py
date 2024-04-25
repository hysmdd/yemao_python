# 多线程L5-生产者与消费者-Condition版本
import threading
import time
import random

total_money = 0
lock = threading.Condition()
cycle = 10
count = 0


class Producer(threading.Thread):
    def run(self) -> None:
        global total_money, cycle, count
        while True:
            lock.acquire()
            money = random.randint(100, 5000)
            if count > cycle:
                lock.release()
                print(f"生产者已经完成工作了")
                break
            total_money += money
            lock.notify_all()
            count += 1
            print(f"生产者{threading.current_thread().name}赚了{money}元")
            print(f"当前余额：{total_money}")
            print("=" * 20)
            lock.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self) -> None:
        while True:
            global total_money, cycle, count
            lock.acquire()
            money = random.randint(100, 5000)
            while total_money < money:
                if count > cycle:
                    print(f"消费者{threading.current_thread().name}想消费{money}元，余额不足，并且生产者不再生产")
                    return
                lock.wait()
            total_money -= money
            print(f"消费者{threading.current_thread().name}消费了{money}元")
            lock.release()
            time.sleep(0.5)


def main():
    for i in range(5):
        th1 = Producer(name=f"生产者{i}号")
        th1.start()
    for j in range(5):
        th2 = Consumer(name=f"消费者{j}号")
        th2.start()


if __name__ == "__main__":
    main()




