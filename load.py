import multiprocessing
from multiprocessing import Pool

def f(x):
    while True:
        x * x

number_of_cores = multiprocessing.cpu_count()

p = Pool(processes=number_of_cores)
p.map(f, range(number_of_cores))
