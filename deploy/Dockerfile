FROM ubuntu:16.04

MAINTAINER Loveloper <loveloper44@gmail.com>

#install libraries for python
RUN apt-get update && apt-get install -y \
    build-essential \
    checkinstall \
    libreadline-gplv2-dev \
    libncursesw5-dev \
    libssl-dev \
    libsqlite3-dev \
    tk-dev \
    libgdbm-dev \
    libc6-dev \
    libbz2-dev \
    wget

#install python
RUN cd /usr/src && wget https://www.python.org/ftp/python/3.5.4/Python-3.5.4.tgz && tar xzf Python-3.5.4.tgz \
    && cd Python-3.5.4 \
    && ./configure \
    && make altinstall

#check version
RUN python3.5 -V
RUN pip3.5 -V

#make project folder in docker environment
RUN mkdir -p /home/project
#copy your file into the project folder in docker environment
COPY server.py /home/project
COPY generator_pb2_grpc.py /home/project
COPY generator_pb2.py /home/project
COPY requirements.txt /home/project

#set working directory
WORKDIR /home/project

#install python libraries
RUN pip3.5 install -r requirements.txt

#The EXPOSE instruction does not actually publish the port.
#In other words, We use this for letting people who use this dockerfile know that this port is used.
#To actually publish the port when running the container, use the -p flag on docker run
EXPOSE 50051

#run server.py
CMD ["python3.5", "server.py"]