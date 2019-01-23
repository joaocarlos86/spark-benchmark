# Apache Spark Playground

This code shows how to use the CUDA SDK to improve the execution time and resource usage of a computationally expensive operation with Spark. To make things even easier, everything is coordinated using Python (+numpy and PySpark)

Code References: https://azure.microsoft.com/en-us/blog/accelerated-spark-on-gpu-enabled-clusters-in-azure/ and https://github.com/Azure/aztk/tree/master/aztk/node_scripts/jupyter-samples

##What is Cuda?

CUDA® is a parallel computing platform and programming model developed by NVIDIA for general computing on graphical processing units (GPUs). With CUDA, developers are able to dramatically speed up computing applications by harnessing the power of GPUs.

In GPU-accelerated applications, the sequential part of the workload runs on the CPU – which is optimized for single-threaded performance – while the compute intensive portion of the application runs on thousands of GPU cores in parallel. When using CUDA, developers program in popular languages such as C, C++, Fortran, Python and MATLAB and express parallelism through extensions in the form of a few basic keywords.

See the [official documentation](https://developer.nvidia.com/cuda-zone)

##What is Spark?

Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine.
Spark offers over 80 high-level operators that make it easy to build parallel apps. And you can use it interactively from the Scala, Python, R, and SQL shells.
Spark powers a stack of libraries including SQL and DataFrames, MLlib for machine learning, GraphX, and Spark Streaming. You can combine these libraries seamlessly in the same application.

See the [official documentation](https://spark.apache.org/)

##What is Numpy?

NumPy is the fundamental package for scientific computing with Python. It contains among other things:

* a powerful N-dimensional array object
* sophisticated (broadcasting) functions
* tools for integrating C/C++ and Fortran code
* useful linear algebra, Fourier transform, and random number capabilities

Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

See the [official documentation](http://www.numpy.org/)