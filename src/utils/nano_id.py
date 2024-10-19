#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module provides a utility function to generate unique Nano IDs using
the `nanoid` library.

The `generate_nano_id` function generates a Nano ID with customizable
characters and size, which can be configured through environment variables.

Environment Variables:
- `NANO_ID_CHARACTERS`: A string of characters to use for generating the
Nano ID. Defaults to
'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.
- `NANO_ID_SIZE`: An integer representing the size of the Nano ID.
Defaults to 25.

Example:
    from app.utils.nano_id import generate_nano_id

    nano_id = generate_nano_id()
    print(nano_id)  # Outputs a unique Nano ID
"""

import os

from nanoid import generate


def generate_nano_id() -> str:
    """
    Generate a unique Nano ID.

    This function generates a Nano ID using the `nanoid` library. The
    characters and size of the Nano ID can be customized using the
    `NANO_ID_CHARACTERS` and `NANO_ID_SIZE` environment variables,
    respectively.

    Returns:
        str: A unique Nano ID.
    """
    id_characters: str = os.getenv(
        'NANO_ID_CHARACTERS',
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    )
    id_size: int = int(os.getenv('NANO_ID_SIZE', '25'))
    new_nano_id: str = generate(id_characters, int(id_size))

    return new_nano_id
