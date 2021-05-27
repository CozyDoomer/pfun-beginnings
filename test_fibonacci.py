import pytest
from fibonacci import Version, fibonacci


def test_with_tail_recursion():
    assert fibonacci(8).run(None) == 21
    assert fibonacci(10).run(None) == 55
    assert fibonacci(20).run(None) == 6765


def test_exponential_recursion():
    assert fibonacci(8, version=Version.EXPONENTIAL_RECURSION).run(None) == 21
    assert fibonacci(10, version=Version.EXPONENTIAL_RECURSION).run(None) == 55
    assert fibonacci(20,
                     version=Version.EXPONENTIAL_RECURSION).run(None) == 6765


def test_invalid_index_exception():

    with pytest.raises(IndexError):
        fibonacci(-1).run(None)
    with pytest.raises(IndexError):
        fibonacci(-12).run(None)


def test_no_exception():
    try:
        fibonacci(0).run(None)
    except Exception as e:
        assert False, f"'fibonacci' raised an exception {e}"

    try:
        fibonacci(1).run(None)
    except Exception as e:
        assert False, f"'fibonacci' raised an exception {e}"
