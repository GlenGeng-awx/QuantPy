from multiprocessing import Process, cpu_count


def print_func(continent='Asia', msg='Hello'):
    print(f'The name of continent is : {continent}, msg={msg}')


if __name__ == "__main__":
    print(f'cpu num: {cpu_count()}')

    names = ['America', 'Europe', 'Africa']
    procs = []

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name, 'fxxk u'))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()
