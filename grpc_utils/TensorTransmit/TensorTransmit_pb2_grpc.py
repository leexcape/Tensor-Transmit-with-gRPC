# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from grpc_utils.TensorTransmit import TensorTransmit_pb2 as grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in grpc_utils/TensorTransmit/TensorTransmit_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TensorTransmitStub(object):
    """The tensor transmission service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetActivationFloat = channel.unary_unary(
                '/TensorTransmit.TensorTransmit/GetActivationFloat',
                request_serializer=grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.TensorRequest_f.SerializeToString,
                response_deserializer=grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.ActivationFloat.FromString,
                _registered_method=True)
        self.GetActivationByte = channel.unary_unary(
                '/TensorTransmit.TensorTransmit/GetActivationByte',
                request_serializer=grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.TensorRequest_b.SerializeToString,
                response_deserializer=grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.ActivationByte.FromString,
                _registered_method=True)


class TensorTransmitServicer(object):
    """The tensor transmission service definition.
    """

    def GetActivationFloat(self, request, context):
        """Sends a tensor
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActivationByte(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TensorTransmitServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetActivationFloat': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActivationFloat,
                    request_deserializer=grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.TensorRequest_f.FromString,
                    response_serializer=grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.ActivationFloat.SerializeToString,
            ),
            'GetActivationByte': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActivationByte,
                    request_deserializer=grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.TensorRequest_b.FromString,
                    response_serializer=grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.ActivationByte.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TensorTransmit.TensorTransmit', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('TensorTransmit.TensorTransmit', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TensorTransmit(object):
    """The tensor transmission service definition.
    """

    @staticmethod
    def GetActivationFloat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TensorTransmit.TensorTransmit/GetActivationFloat',
            grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.TensorRequest_f.SerializeToString,
            grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.ActivationFloat.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetActivationByte(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TensorTransmit.TensorTransmit/GetActivationByte',
            grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.TensorRequest_b.SerializeToString,
            grpc__utils_dot_TensorTransmit_dot_TensorTransmit__pb2.ActivationByte.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
