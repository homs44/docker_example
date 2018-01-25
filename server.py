import generator_pb2
import generator_pb2_grpc
import grpc
import time
from concurrent import futures


class Generator(generator_pb2_grpc.GeneratorServicer):
    def Generate(self, request, context):
        user = request.input
        return generator_pb2.Response(output="Hi "+str(user))


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    generator_pb2_grpc.add_GeneratorServicer_to_server(Generator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    run()


