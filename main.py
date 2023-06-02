import hashlib
from multiprocessing import Pool
import math
import time, os

HASH = '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad' # zyzzx
# HASH = '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b' # apple
# HASH = '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f' # mmmmm

wlist = open('wordlist.txt', 'r').read()
PASSLIST = wlist.split('\n')

found = False
time1 = time.time()

def pwd_find(start, stop):
    for word in range(start, stop):
        print(PASSLIST[word])
        time.sleep(0.1)  # Slows things down so it's easier to see that your system is using more than one core.
        for word in PASSLIST:
                guess = hashlib.sha256(word.encode('utf-8')).hexdigest()
                if guess == HASH:
                        time2 = time.time()
                        timetotal = time2 - time1
                        found = True
                        print(word + " (in " + str(timetotal) + " seconds)")
                        print("")
                        p.terminate
                        p.join
        if not found:
            print("Word was not found")
            p.terminate
            p.join()
            exit()


break_points = []  # List that will have start and stopping points

if __name__ == '__main__':
    cores = int(input("Number of cores to use: "))
    p = Pool(cores)  # Number of processors to utilize.

    for i in range(cores):  # Creates start and stopping points based on length of word list
        break_points.append(
            {"start": math.ceil(len(PASSLIST) / cores * i), "stop": math.ceil(len(PASSLIST) / cores * (i + 1))})

    for i in break_points:  # Cycles through the breakpoints list created above.
        print(i)  # shows the start and stop points.
        a = p.apply_async(pwd_find, kwds=i, args=tuple())  # This will start the separate processes.
    print("Processing..")
    p.close()
    p.join()