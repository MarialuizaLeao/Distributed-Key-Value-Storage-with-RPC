from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class insertRequest(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: int
    value: str
    def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class insertResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: int
    def __init__(self, success: _Optional[int] = ...) -> None: ...

class consultRequest(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: int
    def __init__(self, key: _Optional[int] = ...) -> None: ...

class consultResponse(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class activateRequest(_message.Message):
    __slots__ = ["centralServerID"]
    CENTRALSERVERID_FIELD_NUMBER: _ClassVar[int]
    centralServerID: str
    def __init__(self, centralServerID: _Optional[str] = ...) -> None: ...

class activateResponse(_message.Message):
    __slots__ = ["amountOfActivatedKeys"]
    AMOUNTOFACTIVATEDKEYS_FIELD_NUMBER: _ClassVar[int]
    amountOfActivatedKeys: int
    def __init__(self, amountOfActivatedKeys: _Optional[int] = ...) -> None: ...

class terminateResponse(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: int
    def __init__(self, key: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
