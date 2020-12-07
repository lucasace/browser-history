import abc
from typing import Any

__metaclass__ = type

class Credential(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def username(self) -> Any: ...
    @property
    @abc.abstractmethod
    def password(self) -> Any: ...

class SimpleCredential(Credential):
    def __init__(self, username: Any, password: Any) -> None: ...
    @property
    def username(self): ...
    @property
    def password(self): ...

class EnvironCredential(Credential):
    user_env_var: Any = ...
    pwd_env_var: Any = ...
    def __init__(self, user_env_var: Any, pwd_env_var: Any) -> None: ...
    @property
    def username(self): ...
    @property
    def password(self): ...
