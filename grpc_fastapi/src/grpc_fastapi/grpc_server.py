import grpc
from concurrent import futures
from pb.application_pb2 import ApplicationResponse, UserResponse
from pb.application_pb2_grpc import (
    ApplicationServiceServicer,
    add_ApplicationServiceServicer_to_server,
)


class ApplicationService(ApplicationServiceServicer):
    def ApplicationData(self, request, context):
        return ApplicationResponse(
            data=f"Processed Application ID: {request.application_id}"
        )

    def UserData(self, request, context):
        # Dummy user data
        return UserResponse(name="John Doe", email="john.doe@example.com")


def start_grpc_server():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ApplicationServiceServicer_to_server(ApplicationService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server started on port 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    start_grpc_server()
