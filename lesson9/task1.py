# potok - find sum or row

from multiprocessing import Process, Queue
from datetime import datetime

def sum_ryad(start,end,result):
    res = 0
    for i in range(start,end):
        res +=i
    result.put(res)

def main2():
    result1 = Queue()
    result2 = Queue()
    p1 = Process(target=sum_ryad, args=(1,6000000,result1))
    p2 = Process(target=sum_ryad, args=(6000000,10000000, result2))
    time_start = datetime.now()
    p1.start()
    p2.start()
    p1.join() # join stop main still p1 doesn't finish
    p2.join()
    total = result1.get() + result2.get()
    time_end = datetime.now()
    print(total)
    print("time=",time_end-time_start)

if __name__=="__main__":
    main2()

#main2()




