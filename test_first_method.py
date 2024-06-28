import pytest
from unit_tests.hw_4 import Utilities


@pytest.mark.parametrize('number, expected', [
    (1, True),
    (-2, False),
    (0, False),
    (4, False)
])
def test_is_positive(number, expected):
    assert Utilities.is_positive(number) == expected
