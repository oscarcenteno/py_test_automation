import pytest
from .inc_dec import increment, decrement    # The code to test


@pytest.mark.unit
def test_increment():
    assert increment(3) == 4

# This test is designed to fail for demonstration purposes.
@pytest.mark.unit
def test_decrement():
    result = decrement(3)
    assert result == 4
