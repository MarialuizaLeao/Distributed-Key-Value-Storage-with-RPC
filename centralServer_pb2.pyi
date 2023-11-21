from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class registerRequest(_message.Message):
    __slots__ = ["serverID", "keyList"]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    KEYLIST_FIELD_NUMBER: _ClassVar[int]
    serverID: str
    keyList: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, serverID: _Optional[str] = ..., keyList: _Optional[_Iterable[int]] = ...) -> None: ...

class registerResponse(_message.Message):
    __slots__ = ["amountOfRegisteredKeys"]
    AMOUNTOFREGISTEREDKEYS_FIELD_NUMBER: _ClassVar[int]
    amountOfRegisteredKeys: int
    def __init__(self, amountOfRegisteredKeys: _Optional[int] = ...) -> None: ...

class mapRequest(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: int
    def __init__(self, key: _Optional[int] = ...) -> None: ...

class mapResponse(_message.Message):
    __slots__ = ["serverID"]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    serverID: str
    def __init__(self, serverID: _Optional[str] = ...) -> None: ...

class terminateResponse(_message.Message):
    __slots__ = ["amountOfRegisteredKeys"]
    AMOUNTOFREGISTEREDKEYS_FIELD_NUMBER: _ClassVar[int]
    amountOfRegisteredKeys: int
    def __init__(self, amountOfRegisteredKeys: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
