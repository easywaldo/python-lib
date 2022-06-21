import time
import sched

start = time.time()

def print_a(a):
    print(time.time() - start)
    print(a)

def print_b(b):
    print(time.time() - start)
    print(b)
    
def print_c(c):
    print(time.time() - start)
    print(c)
    
s = sched.scheduler()
s.enter(5, 1, print_a, ('A', ))
s.enter(3, 1, print_b, ('B', ))
s.enter(7, 1, print_c, ('C', ))
s.run()    
