import threading
import time

def worker(num):
    print(f"Worker thread {num} started")
    time.sleep(2) # Simulate some work being done
    print(f"Worker thread {num} finished")


threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads have completed.")