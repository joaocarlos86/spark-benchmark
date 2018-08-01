import math
import time
import numpy as np
from numba import cuda, vectorize, jit
import timeit
from numba import vectorize
from pyspark import SparkContext

number=10000000

@vectorize(['float32(float32, float32)'], target='cuda')
def gpu_pow(a, b):
    return a ** b

def gpu_work(vec_size):
    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)
    c = gpu_pow(a, b)

sc = SparkContext('local[50]', 'test')
rdd = sc.parallelize(list([number]*100))
print("Partitions", rdd.getNumPartitions())
res = rdd.map(lambda x : gpu_work(x))
res.collect()
