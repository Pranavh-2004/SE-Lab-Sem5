import pytest
from order_processor import calculate_discount, update_order_status

#Example test cases:
def test_regular_low_amount():
    assert calculate_discount("regular", 500) == 0

def test_premium_discount():
    assert calculate_discount("premium", 2000) == 200

#Write the rest of the test cases so that the code is 90- 100% covered.

