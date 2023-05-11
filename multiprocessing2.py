from multiprocessing import Process, Semaphore

from time import sleep

def printare_range(de_la:int, pana_la:int, sem:Semaphore):
    # barrier.wait()
    with sem:
        for x in range(de_la, pana_la):
            sleep(0.05)
            print(x)

def run_processes(num_processes :int):
    sem = Semaphore(num_processes)
    processes = []
    # for i in range(num_processes):
    #     processes.append(Process(target = printare_range, args = (20,40,sem)))
    processes = [Process(target = printare_range, args = (20,40,sem)) for i in range(num_processes)]
    for process in processes:
        process.start()

    # barrier.wait()
    for process in processes:
        process.join()

if __name__ == "__main__":
    run_processes(5)