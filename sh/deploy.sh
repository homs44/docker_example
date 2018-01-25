#!/bin/sh

cp server.py deploy/
cp generator_pb2_grpc.py deploy/
cp generator_pb2.py deploy/
cp requirements.txt deploy/

cd deploy
docker build -t generator:latest .

rm -rf server.py
rm -rf generator_pb2_grpc.py
rm -rf generator_pb2.py
rm -rf requirements.txt

