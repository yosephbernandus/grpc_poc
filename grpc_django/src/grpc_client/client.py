import grpc
from django.conf import settings
from pb.application_pb2 import ApplicationRequest, UserRequest
from pb.application_pb2_grpc import ApplicationServiceStub


def get_application_data(application_id: int):
    # channel = grpc.insecure_channel("localhost:50051")
    # channel = grpc.insecure_channel("127.0.0.1:50051")
    channel = grpc.insecure_channel(settings.GRPC_SERVER)
    stub = ApplicationServiceStub(channel)
    request = ApplicationRequest(application_id=application_id)
    return stub.ApplicationData(request)


def get_user_data(user_id: int):
    channel = grpc.insecure_channel(settings.GRPC_SERVER)
    stub = ApplicationServiceStub(channel)
    request = UserRequest(user_id=user_id)
    return stub.UserData(request)
