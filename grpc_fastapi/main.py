from typing import Union
import grpc
from concurrent import futures
from fastapi import FastAPI
from grpc_interceptor import ExceptionToStatusInterceptor
from pb.sample_pb2_grpc import add_GreeterServicer_to_server, GreeterServicer

app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


class GreeterService(GreeterServicer):
    pass


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
