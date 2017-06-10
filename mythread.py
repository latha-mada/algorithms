#!/usr/bin/python
import threading


class PrimeNumber(threading.Thread):
    prime_numbers = {} 
    lock = threading.Lock()
    
    def __init__(self, number): 
        threading.Thread.__init__(self) 
        self.Number = number
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[number] = "None" 
        PrimeNumber.lock.release() 
 
    def run(self): 
        counter = 2
        res = True
        while counter*counter < self.Number and res: 
            if self.Number % counter == 0: 
               res = False 
               break
            counter += 1 
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[self.Number] = res 
        PrimeNumber.lock.release() 
threads = [] 
count = 10
while count>0: 
    input = long(raw_input("number: ")) 
    if input < 1: 
        break 
 
    thread = PrimeNumber(input) 
    threads += [thread] 
    thread.start()
    count -= 1 
 
print threads
print PrimeNumber.prime_numbers
for x in threads: 
    x.join()

