import pytest

from dummy_plugin import classify_count


def test_empty():
    assert classify_count(0) == "EMPTY"

def test_small():
    assert classify_count(3) == "SMALL"

def test_large():
    assert classify_count(12) == "LARGE"

def test_negative_raises():
    with pytest.raises(ValueError):
        classify_count(-1)