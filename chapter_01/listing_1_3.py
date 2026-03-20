import threading
import time


def hello_from_thread():
    print(f'Hello from thread "{threading.current_thread().name}"!')
    time.sleep(3)
    print(f"Ta Da! from {threading.current_thread().name}")


hello_thread = threading.Thread(target=hello_from_thread, name="other_thread")
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python is currently running {total_threads} thread(s)')
print(f'The current thread is {thread_name}')

# join нужен, чтобы дождаться все threads, которые начались выше.
# такой некий стопер
hello_thread.join()
print("after join")
