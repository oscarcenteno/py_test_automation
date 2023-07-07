import pytest
from .questions import get_state

@pytest.mark.api
def test_can_get_state():
    # Arrange
    country = 'us'
    zip_code = '90210'
    expected_state = 'California'

    # Act
    actual_state = get_state(country, zip_code)

    # Assert
    assert actual_state == expected_state
