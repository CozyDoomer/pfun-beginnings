from enum import Enum
from timeit import default_timer as timer
from typing import Union
from pfun.effect import Effect, error, success


class Version(Enum):
    EXPONENTIAL_RECURSION = 1
    TAIL_OPTIMIZED_RECURSION = 2


def recursive_fib(n: int) -> int:
    if n <= 1:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)


def tail_recursive_fib(n: int) -> int:
    def fib(count: int, curr: int, prev: int):
        if count <= 0:
            return prev
        return fib(count=count - 1, curr=prev + curr, prev=curr)

    return fib(count=n, curr=1, prev=0)


def fibonacci(
    n,
    version: Version = Version.TAIL_OPTIMIZED_RECURSION
) -> Effect[int, Union[IndexError, NotImplementedError], int]:
    result: Effect[int, Union[IndexError, NotImplementedError], int]
    if n < 0:
        result = error(IndexError("Provided index has to be > 0"))
    elif version == Version.TAIL_OPTIMIZED_RECURSION:
        result = success(tail_recursive_fib(n))
    elif version == Version.EXPONENTIAL_RECURSION:
        result = success(recursive_fib(n))
    else:
        result = error(NotImplementedError(f"{version} not implemented"))

    return result


def benchmark():
    # warmup
    fibonacci(10).run(None)
    fibonacci(20).run(None)

    s = timer()
    print(fibonacci(20).run(None))
    print("tail recursion version:")
    print(float(timer() - s))

    s = timer()
    print(fibonacci(20, version=Version.EXPONENTIAL_RECURSION).run(None))
    print("exponential recursion version:")
    print(float(timer() - s))
