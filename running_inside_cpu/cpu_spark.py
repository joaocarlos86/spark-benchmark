import math
import time
import numpy as np
from numba import cuda, vectorize, jit
import timeit
from numba import vectorize
from pyspark import SparkContext

number=10000000

if not cuda.is_available():
    print("CUDA is not available")
else:
    print("CUDA is available")

def cpu_pow(a,b):
    return a ** b

def cpu_work(vec_size):
    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    c = cpu_pow(a, b)

sc = SparkContext('local[8]', 'test')
rdd = sc.parallelize(list([number]*100))
print("Partitions", rdd.getNumPartitions())

res = rdd.map(lambda x : cpu_work(x))
res.collect()
