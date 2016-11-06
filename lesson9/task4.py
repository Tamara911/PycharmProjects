# skrypachi

from multiprocessing import Process, Queue, Condition
import time

def veolonist(tumb_violin, tumb_bow, mutex_violin, mutex_bow, name):
    while True:
        mutex_violin.acquire()
        while tumb_violin.qsize() == 0:
            mutex_violin.wait()
        tumb_violin.get()
        print("Violinist "+ name + "took the violin")
        mutex_violin.release()
        mutex_bow.acquire()
        while tumb_bow.qsize() == 0:
            mutex_bow.wait()
        tumb_bow.get()
        print("Violinist " + name + "took the bow")
        mutex_bow.release()
        print("Violinist "+ name +" is playing")

        time.sleep(3)

        mutex_violin.acquire()
        tumb_violin.put("violine")
        mutex_violin.notify_all()
        mutex_violin.release()

        mutex_bow.acquire()
        tumb_bow.put("bow")
        mutex_bow.notify_all()
        mutex_bow.release()

def main():
    tumb_violin = Queue()
    tumb_violin.put("violine")
    tumb_violin.put("violine")
    tumb_violin.put("violine")
    tumb_bow = Queue()
    tumb_bow.put("bow")
    tumb_bow.put("bow")
    tumb_bow.put("bow")

    mutex_violin = Condition()
    mutex_bow = Condition()

    violonist1 = Process(target=veolonist, args=(tumb_violin, tumb_bow, mutex_violin, mutex_bow, "Violonist1"))
    violonist2 = Process(target=veolonist, args=(tumb_violin, tumb_bow, mutex_violin, mutex_bow, "Violonist2"))
    violonist3 = Process(target=veolonist, args=(tumb_violin, tumb_bow, mutex_violin, mutex_bow, "Violonist3"))
    violonist4 = Process(target=veolonist, args=(tumb_violin, tumb_bow, mutex_violin, mutex_bow, "Violonist4"))
    violonist5 = Process(target=veolonist, args=(tumb_violin, tumb_bow, mutex_violin, mutex_bow, "Violonist5"))
    violonist6 = Process(target=veolonist, args=(tumb_violin, tumb_bow, mutex_violin, mutex_bow, "Violonist6"))

    violonist1.start()
    violonist2.start()
    violonist3.start()
    violonist4.start()
    violonist5.start()
    violonist6.start()
    violonist1.join()

if __name__=="__main__":
    main()





