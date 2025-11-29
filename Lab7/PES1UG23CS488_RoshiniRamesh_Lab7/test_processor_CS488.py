import pytest
from order_processor import calculate_discount, update_order_status

#Example test cases:
def test_regular_low_amount():
    assert calculate_discount("regular", 500) == 0

def test_premium_discount():
    assert calculate_discount("premium", 2000) == 200

# Test cases for calculate_discount function

def test_regular_high_amount():
    """Test regular customer with amount > 1000 gets 5% discount"""
    assert calculate_discount("regular", 2000) == 100

def test_regular_exact_threshold():
    """Test regular customer with amount exactly at 1000"""
    assert calculate_discount("regular", 1000) == 0

def test_premium_various_amounts():
    """Test premium customer gets 10% discount regardless of amount"""
    assert calculate_discount("premium", 500) == 50
    assert calculate_discount("premium", 10000) == 1000

def test_vip_low_amount():
    """Test VIP customer with amount <= 5000 gets 10% discount"""
    assert calculate_discount("vip", 3000) == 300
    assert calculate_discount("vip", 5000) == 500

def test_vip_high_amount():
    """Test VIP customer with amount > 5000 gets 20% discount"""
    assert calculate_discount("vip", 6000) == 1200
    assert calculate_discount("vip", 10000) == 2000

def test_unknown_customer_type():
    """Test that unknown customer type raises ValueError"""
    with pytest.raises(ValueError, match="Unknown customer type"):
        calculate_discount("unknown", 1000)
    with pytest.raises(ValueError, match="Unknown customer type"):
        calculate_discount("gold", 500)

# Test cases for update_order_status function

def test_pending_paid_order():
    """Test pending order that is paid moves to processing"""
    order = {"status": "pending", "paid": True, "items_available": True}
    result = update_order_status(order)
    assert result == "processing"
    assert order["status"] == "processing"

def test_pending_unpaid_order():
    """Test pending order that is not paid moves to awaiting_payment"""
    order = {"status": "pending", "paid": False, "items_available": True}
    result = update_order_status(order)
    assert result == "awaiting_payment"
    assert order["status"] == "awaiting_payment"

def test_processing_items_available():
    """Test processing order with items available moves to shipped"""
    order = {"status": "processing", "paid": True, "items_available": True}
    result = update_order_status(order)
    assert result == "shipped"
    assert order["status"] == "shipped"

def test_processing_items_unavailable():
    """Test processing order with items unavailable moves to backorder"""
    order = {"status": "processing", "paid": True, "items_available": False}
    result = update_order_status(order)
    assert result == "backorder"
    assert order["status"] == "backorder"

def test_order_status_other_states():
    """Test orders with other statuses remain unchanged"""
    order = {"status": "shipped", "paid": True, "items_available": True}
    result = update_order_status(order)
    assert result == "shipped"
    assert order["status"] == "shipped"
