from multiprocessing import Process, Queue
import time


def worker(task_id: int, queue: Queue):
    # Simulate a task by sleeping for a random amount of time
    time.sleep(task_id)
    result = f"Task {task_id} completed"
    queue.put(result)


if __name__ == '__main__':
    num_tasks = 5
    queue = Queue()
    processes = []

    # Create and start processes
    for i in range(num_tasks):
        p = Process(target=worker, args=(i, queue))
        p.start()
        processes.append(p)

    # Join processes
    for p in processes:
        p.join()

    # Collect results from the queue
    results = []
    while not queue.empty():
        results.append(queue.get())

    # Print results
    for result in results:
        print(result)
