# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import torch
import grpc
from grpc_utils.TensorTransmit import TensorTransmit_pb2
from grpc_utils.TensorTransmit import TensorTransmit_pb2_grpc

activation_list = [torch.rand((197, 768)) for i in range(12)]
class TensorTransmit(TensorTransmit_pb2_grpc.TensorTransmitServicer):
    def GetActivationFloat(self, request, context):
        flat_tensor = activation_list[request.layer_index].cpu().flatten().numpy()
        tensor_shape = str(activation_list[request.layer_index].cpu().numpy().shape)
        return TensorTransmit_pb2.ActivationFloat(tensor=flat_tensor, shape_f=tensor_shape)

    def GetActivationByte(self, request, context):
        flat_tensor = activation_list[request.layer_index].cpu().flatten().numpy()
        flat_tensor_byte = flat_tensor.tobytes()
        tensor_shape = str(activation_list[request.layer_index].cpu().numpy().shape)
        return TensorTransmit_pb2.ActivationByte(buffer=flat_tensor_byte, shape_b=tensor_shape, dtype=str(flat_tensor.dtype))


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TensorTransmit_pb2_grpc.add_TensorTransmitServicer_to_server(TensorTransmit(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
