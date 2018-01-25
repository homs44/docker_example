import generator_pb2
import generator_pb2_grpc
import grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = generator_pb2_grpc.GeneratorStub(channel)
    response = stub.Generate(generator_pb2.Request(input='Ingyu Yoon'))
    print("client received: " + response.output)


if __name__ == "__main__":
    run()
