from abc import ABC, abstractmethod
from typing import Optional, Sequence, Any
from ds._validators import _validate_instantiation_from_sequence


class _Heap(ABC):
    def __new__(cls, _from: Optional[Sequence] = None) -> "_Heap":
        _validate_instantiation_from_sequence(sequence=_from, data_structure="heap")
        return super().__new__(cls)

    @abstractmethod
    def insert(self, item: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def pop(self) -> Any:
        raise NotImplementedError
