import threading
import multiprocessing
import time

"""This is almost entirely due to the GIL and the overhead of creating and managing threads. 
While it is true the threads run concurrently, only one of them is allowed to run Python code at a time due to the lock. 
This leaves the other thread in a waiting state until the first one completes, 
which completely negates the value of multiple threads."""

def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f'fib({number}) is {fib(number)}')


def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))

    fortieth_thread.start()
    forty_first_thread.start()

    fortieth_thread.join()
    forty_first_thread.join()

def fibs_with_processes():
    fortieth_process = multiprocessing.Process(target=print_fib, args=(40,))
    forty_first_process = multiprocessing.Process(target=print_fib, args=(41,))

    fortieth_process.start()
    forty_first_process.start()

    fortieth_process.join()
    forty_first_process.join()


if __name__ == "__main__":
    start_threads = time.time()

    fibs_with_threads()

    end_threads = time.time()

    print(f"Threads took {end_threads - start_threads:.4f} seconds.")

    start_processes = time.time()

    fibs_with_processes()

    end_processes = time.time()

    print(f"Processes took {end_processes - start_processes:.4f} seconds.")