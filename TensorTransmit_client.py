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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging
import numpy as np
import grpc
import torch
import time

from grpc_utils.TensorTransmit import TensorTransmit_pb2
from grpc_utils.TensorTransmit import TensorTransmit_pb2_grpc


def run(n_tensors_f=1, n_tensors_b=1, dtype="float32"):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to grab tensor from server ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = TensorTransmit_pb2_grpc.TensorTransmitStub(channel)
        # Transmission with tensor
        start_time = time.time()
        response_f = stub.GetActivationFloat(TensorTransmit_pb2.TensorRequest_f(n_tensors=n_tensors_f))
        latency_f = time.time() - start_time
        shape_f = tuple(int(x.strip()) for x in response_f.shape_f.strip("()").split(","))
        tensor_f = torch.tensor(np.reshape(response_f.tensor, shape_f))

        # Transmission with raw bytes
        start_time = time.time()
        response_b = stub.GetActivationByte(TensorTransmit_pb2.TensorRequest_b(n_tensors=n_tensors_b, desired_dtype=dtype))
        latency_b = time.time() - start_time
        shape_b = tuple(int(x.strip()) for x in response_b.shape_b.strip("()").split(","))
        array_b = np.frombuffer(response_b.buffer, response_b.dtype)
        tensor_b = torch.tensor(np.reshape(array_b, shape_b))

    print("The Tensor is received successfully!")
    print("Received size of numerical data: ", response_f.shape_f)
    print("Received size of raw byte: ", response_b.shape_b)
    print("The transmission latency of tensor transmission(", tensor_f.dtype, "): ", latency_f)
    print("The transmission latency of raw bytes transmission(", tensor_b.dtype, "): ", latency_b)
    return latency_f, latency_b


if __name__ == "__main__":
    logging.basicConfig()
    run(2, 3, "float32")
