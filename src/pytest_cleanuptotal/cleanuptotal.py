from typing import Generator
import pytest
from pytest_cleanuptotal.cleanup import Cleanup

@pytest.fixture
def cleanuptotal() -> Generator[Cleanup, None, None]:
    cleanup = Cleanup()
    yield cleanup
    cleanup.finalize()
