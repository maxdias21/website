from typing import Dict, List


def min_length(value: str, min_length_value: int) -> bool:
    return len(value) < min_length_value


def validate_min_length_multiple(fields: List[Dict[str, Dict[str, str]]], min_length):
    errors = {}
    for field in fields:
        for key_sub, value_sub in field.items():
            if len(value_sub) < min_length:
                errors[key_sub] = value_sub['error_message']

    return None if len(errors) == 0 else errors
