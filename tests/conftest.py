from stuff.accum import Accumlator
import pytest


@pytest.fixture
def accum():
    return Accumlator()


@pytest.fixture
def accum2():
    print("SET UP ()")
    yield Accumlator()
    print("CLEAN()")


# Before All tests in the Package
@pytest.fixture
def accum3(scope="session"):
    return Accumlator() 

# Before Each All tests in the Package
@pytest.fixture
def accum4(scope="function"):
    return Accumlator()    