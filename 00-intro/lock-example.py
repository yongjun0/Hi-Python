import threading

lock = threading.Lock()
def function1():
    c = '\033[91m'  # red
    c = '\033[36m'  # cyan
    for i in range(10):
        lock.acquire ()  # lock!!
        for word in ['Hello', 'from', 'the', 'first', 'function\n']:
            print(f' {c}{word}', end='')
        
        lock.release ()

def function2():
    c = '\033[92m'  # green
    for i in range(10):
        lock.acquire ()
        for word in ['Hello', 'from', 'the', 'second', 'function\n']:
            print(f' {c}{word}', end='')
            
        lock.release ()  # unlock!


thread_1 = threading.Thread(target=function1)
thread_2 = threading.Thread(target=function2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
