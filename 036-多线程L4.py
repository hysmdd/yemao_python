# 多线程L4-生产者和消费者-Lock版
import threading
import random
import time

total_money = 0
lock = threading.Lock()
cycle_time = 10
count = 0


class Producer(threading.Thread):
    def run(self) -> None:
        global total_money, cycle_time, count
        while True:
            lock.acquire()
            money = random.randint(100, 5000)
            if count > cycle_time:
                print(f"生产者已经完成工作了")
                lock.release()
                break
            total_money += money
            count += 1
            print(f"生产者{threading.current_thread().name}赚了{money}元")
            print(f"当前余额：{total_money}")
            print("=" * 20)
            lock.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self) -> None:
        while True:
            global total_money, count, cycle_time
            lock.acquire()
            money = random.randint(100, 5000)
            if total_money > money:
                total_money -= money
                print(f"消费者{threading.current_thread().name}消费了{money}元")
                print(f"当前余额：{total_money}")
                print("=" * 20)
            else:
                if count > cycle_time:
                    lock.release()
                    print(f"消费者{threading.current_thread().name}想消费{money}元，余额不足，并且生产者不再生产")
                    break
                print(f"消费者{threading.current_thread().name}想消费{money}元，余额不足，余额只有{total_money}元")
            lock.release()
            time.sleep(0.5)


def main():
    for i in range(5):
        th1 = Producer(name=f"生产者{i}号")
        th1.start()

    for j in range(5):
        th2 = Consumer(name=f"消费者{j}号")
        th2.start()


if __name__ == '__main__':
    main()
