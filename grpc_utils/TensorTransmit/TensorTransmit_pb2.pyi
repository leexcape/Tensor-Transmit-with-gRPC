from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TensorRequest_f(_message.Message):
    __slots__ = ("n_tensors",)
    N_TENSORS_FIELD_NUMBER: _ClassVar[int]
    n_tensors: int
    def __init__(self, n_tensors: _Optional[int] = ...) -> None: ...

class TensorRequest_b(_message.Message):
    __slots__ = ("n_tensors", "desired_dtype")
    N_TENSORS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_DTYPE_FIELD_NUMBER: _ClassVar[int]
    n_tensors: int
    desired_dtype: str
    def __init__(self, n_tensors: _Optional[int] = ..., desired_dtype: _Optional[str] = ...) -> None: ...

class ActivationFloat(_message.Message):
    __slots__ = ("tensor", "shape_f")
    TENSOR_FIELD_NUMBER: _ClassVar[int]
    SHAPE_F_FIELD_NUMBER: _ClassVar[int]
    tensor: _containers.RepeatedScalarFieldContainer[float]
    shape_f: str
    def __init__(self, tensor: _Optional[_Iterable[float]] = ..., shape_f: _Optional[str] = ...) -> None: ...

class ActivationByte(_message.Message):
    __slots__ = ("buffer", "shape_b", "dtype")
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    SHAPE_B_FIELD_NUMBER: _ClassVar[int]
    DTYPE_FIELD_NUMBER: _ClassVar[int]
    buffer: bytes
    shape_b: str
    dtype: str
    def __init__(self, buffer: _Optional[bytes] = ..., shape_b: _Optional[str] = ..., dtype: _Optional[str] = ...) -> None: ...
