# -*- coding: utf-8 -*-
import _thread
import threading


def fun():
    for key in range(20):
        x2 = yield key
        print('good', x2)


def thread_demo():
    threading.Thread().start()
    _thread.start_new_thread()


import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

# if __name__ == '__main__':
#     a = fun()
#     for i in range(30):
#         x = a.__next__()
#         print(x)
