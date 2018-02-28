import threading
import time
import random

counter = 1


class hybridSpinLock:
    def __init__(self):
        self.lock_var = threading.Lock()
        self.threshold = 1
    def lock(self):
        #stalling
        start = time.time()
        elapsed = 0
        while (self.lock_var.acquire(False)==False):
            elapsed = time.time() - start
            if elapsed >= 2*self.threshold:
                self.lock_var.acquire()  # blocking lock
                break
        #update the threshold value
        self.threshold += (elapsed - self.threshold)/8
    def release(self):
        self.threshold=1
        self.lock_var.release()



def workerA():
  global counter
  lo.lock()
  #o.acquire()
  try:
    while counter < 1000:
      counter += 1
      print("Worker A is incrementing counter to {}".format(counter))

  finally:
      lo.release()
      #o.release()

def workerB():
  global counter
  lo.lock()
  #o.acquire()
  try:
    while counter > -1000:
      counter -= 1
      print("Worker B is decrementing counter to {}".format(counter))

  finally:
    lo.release()
    #o.release()

lo=hybridSpinLock()
#o=threading.Lock()
def main():

  t0 = time.time()
  thread1 = threading.Thread(target=workerA)
  thread2 = threading.Thread(target=workerB)
  thread11 = threading.Thread(target=workerA)
  thread22 = threading.Thread(target=workerB)
  thread12 = threading.Thread(target=workerA)
  thread21 = threading.Thread(target=workerB)

  thread1.start()
  thread2.start()
  thread11.start()
  thread22.start()
  thread12.start()
  thread21.start()
  thread1.join()
  thread2.join()
  thread11.join()
  thread22.join()
  thread12.join()
  thread21.join()

  t1 = time.time()

  print("Execution Time {}".format(t1-t0))

if __name__ == '__main__':
  main()
