from typing import Any, Sequence


def _validate_index(index: int, lower_bound: int, upper_bound: int) -> None:
    if not isinstance(index, int):
        raise TypeError(
            f"Wrong type provided for index. Expected type `int`, got type {type(index)}"
        )
    if not (lower_bound <= index <= upper_bound):
        raise IndexError(
            f"Index out of range. Chose an index between [{lower_bound}, {upper_bound}]."
        )


def _validate_instantiation_from_sequence(sequence: Any, data_structure: str):
    if not isinstance(sequence, Sequence) and sequence:
        raise TypeError(
            f"Creation of the data structure {data_structure} from type {type(sequence)} not supported."
        )
