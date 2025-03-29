import time, random, threading, queue

file_list = [
    "image_0001.jpg",
    "image_0002.jpg",
    "image_0003.jpg",
    "image_0004.jpg",
    "image_0005.jpg",
    "image_0006.jpg",
    "image_0007.jpg",
    "image_0008.jpg",
    "image_0009.jpg",
    "image_0010.jpg"
]

# onvert our list to a queue
job_queue = queue.Queue()
for i in file_list:
    job_queue.put(i)

def worker():
    while not job_queue.empty():
        file = job_queue.get()
        print(f"Converting {file}...")
        time.sleep(random.randint(6, 30))
        print(f"Convert {file} finished!")
        job_queue.task_done()

# start 10 workers
for _ in range(10):
    t = threading.Thread(target=worker)
    t.start()