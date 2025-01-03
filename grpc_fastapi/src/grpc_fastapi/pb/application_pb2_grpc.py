# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
import warnings

import pb.application_pb2 as application__pb2

GRPC_GENERATED_VERSION = "1.68.1"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in application_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class ApplicationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ApplicationData = channel.unary_unary(
            "/ApplicationService/ApplicationData",
            request_serializer=application__pb2.ApplicationRequest.SerializeToString,
            response_deserializer=application__pb2.ApplicationResponse.FromString,
            _registered_method=True,
        )
        self.UserData = channel.unary_unary(
            "/ApplicationService/UserData",
            request_serializer=application__pb2.UserRequest.SerializeToString,
            response_deserializer=application__pb2.UserResponse.FromString,
            _registered_method=True,
        )


class ApplicationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ApplicationData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UserData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ApplicationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ApplicationData": grpc.unary_unary_rpc_method_handler(
            servicer.ApplicationData,
            request_deserializer=application__pb2.ApplicationRequest.FromString,
            response_serializer=application__pb2.ApplicationResponse.SerializeToString,
        ),
        "UserData": grpc.unary_unary_rpc_method_handler(
            servicer.UserData,
            request_deserializer=application__pb2.UserRequest.FromString,
            response_serializer=application__pb2.UserResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "ApplicationService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("ApplicationService", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class ApplicationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ApplicationData(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ApplicationService/ApplicationData",
            application__pb2.ApplicationRequest.SerializeToString,
            application__pb2.ApplicationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def UserData(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ApplicationService/UserData",
            application__pb2.UserRequest.SerializeToString,
            application__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
