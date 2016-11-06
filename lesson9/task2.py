# synhronize of potoc

from multiprocessing import Process, Queue, Condition

# 2 func - producer and 2 - consumer

def producer(tumb, mutex, name):
    while True:
        mutex.acquire() # set flag - change from 0 to 1
        while tumb.qsize() >= 4:
            mutex.wait() # block vypolnenie - change on 0
        tumb.put("element")
        print("Produce " + name + " put the element")
        mutex.notify_all() # knock to door
        mutex.release() # snyali flag

def consumer(tumb, mutex, name):
    while True:
        mutex.acquire()
        while tumb.qsize() == 0:
            mutex.wait()
        tumb.get() # take smth
        print("consumer "+ name +" remove the element")
        mutex.notify_all
        mutex.release()


def main():
    tumb = Queue()
    mutex = Condition()
    producer1 = Process(target=producer, args=(tumb, mutex, "Producer1"))
    producer2 = Process(target=producer, args=(tumb, mutex, "Producer2"))
    producer3 = Process(target=producer, args=(tumb, mutex, "Producer3"))
    consumer1 = Process(target=consumer, args=(tumb, mutex, "consumer1"))
    consumer2 = Process(target=consumer, args=(tumb, mutex, "consumer2"))
    producer1.start()
    producer2.start()
    producer3.start()
    consumer1.start()
    consumer2.start()
    producer1.join()

if __name__=="__main__":
    main()
