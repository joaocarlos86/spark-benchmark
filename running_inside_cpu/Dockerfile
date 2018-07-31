FROM ubuntu:18.04

#adding numpy
RUN ["apt", "update"]
RUN ["apt", "install", "-y" , "python-numpy", "git", "openjdk-8-jdk", "python-pip"]

RUN ["mkdir", "-p", "/opt/local/dev/numpy/"]

ADD requirements /opt/local/dev/

RUN ["pip", "install", "-r", "/opt/local/dev/requirements"]
ADD cpu_spark.py /opt/local/dev/numpy/

CMD ["time", "python", "/opt/local/dev/numpy/cpu_spark.py"]
