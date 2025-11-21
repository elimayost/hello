"""
Tests for hello module.
"""

import hello


def test_hello() -> None:
    """
    Test for hello function.
    """
    if hello.main() != "Hello from hello!":
        raise ValueError
