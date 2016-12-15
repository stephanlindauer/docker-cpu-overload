import multiprocessing
from multiprocessing import Pool

def load(x):
    while True:
        x * x

number_of_cores = multiprocessing.cpu_count()

pool = Pool(processes=number_of_cores)
pool.map(load, range(number_of_cores))
