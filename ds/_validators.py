from typing import Any, Sequence
from collections.abc import Hashable


def _validate_index(index: int, lower_bound: int, upper_bound: int) -> None:
    if not isinstance(index, int):
        raise TypeError(
            f"Wrong type provided for index. Expected type `int`, got type {type(index)}"
        )
    if not (lower_bound <= index <= upper_bound):
        raise IndexError(
            f"Index out of range. Chose an index between [{lower_bound}, {upper_bound}]."
        )


def _validate_instantiation_from_sequence(sequence: Any, data_structure: str) -> None:
    if not isinstance(sequence, Sequence) and sequence:
        raise TypeError(
            f"Creation of the data structure {data_structure} from type {type(sequence)} not supported."
        )


def _validate_capacity(capacity: int) -> None:
    if not isinstance(capacity, int):
        raise TypeError(
            f"Wrong type provided for capacity. Expected type `int`, got type {type(capacity)}."
        )
    if capacity <= 0:
        raise ValueError("Capacity must be greater than 0.")


def _validate_hashable_key(key: Any) -> None:
    if not isinstance(key, Hashable):
        raise TypeError("The provided key must be a hashable object.")
