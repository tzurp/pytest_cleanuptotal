import pytest

from .cleanup import Cleanup

@pytest.fixture
def cleanuptotal() -> Cleanup:
    cleanup = Cleanup()
    yield cleanup
    cleanup.finalize()
