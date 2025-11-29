import pytest
from order_processor import calculate_discount, update_order_status

# Example test cases:
def test_regular_low_amount():
    assert calculate_discount("regular", 500) == 0

def test_premium_discount():
    assert calculate_discount("premium", 2000) == 200

# Additional test cases for calculate_discount to cover all branches

def test_regular_high_amount():
    """Test regular customer with amount > 1000 (5% discount)"""
    assert calculate_discount("regular", 1001) == pytest.approx(50.05)
    assert calculate_discount("regular", 2000) == pytest.approx(100)

def test_regular_exactly_1000():
    """Test regular customer with amount exactly 1000 (no discount)"""
    assert calculate_discount("regular", 1000) == 0

def test_vip_low_amount():
    """Test VIP customer with amount <= 5000 (10% discount)"""
    assert calculate_discount("vip", 500) == pytest.approx(50)
    assert calculate_discount("vip", 5000) == pytest.approx(500)

def test_vip_high_amount():
    """Test VIP customer with amount > 5000 (20% discount)"""
    assert calculate_discount("vip", 5001) == pytest.approx(1000.2)
    assert calculate_discount("vip", 10000) == pytest.approx(2000)

def test_invalid_customer_type():
    """Test invalid customer type raises ValueError"""
    with pytest.raises(ValueError, match="Unknown customer type"):
        calculate_discount("gold", 1000)
    
    with pytest.raises(ValueError, match="Unknown customer type"):
        calculate_discount("unknown", 500)

# Test cases for update_order_status to cover all branches

def test_update_status_pending_paid():
    """Test pending order that is paid -> processing"""
    order = {"status": "pending", "paid": True}
    assert update_order_status(order) == "processing"
    assert order["status"] == "processing"

def test_update_status_pending_not_paid():
    """Test pending order that is not paid -> awaiting_payment"""
    order = {"status": "pending", "paid": False}
    assert update_order_status(order) == "awaiting_payment"
    assert order["status"] == "awaiting_payment"

def test_update_status_processing_items_available():
    """Test processing order with items available -> shipped"""
    order = {"status": "processing", "items_available": True}
    assert update_order_status(order) == "shipped"
    assert order["status"] == "shipped"

def test_update_status_processing_items_not_available():
    """Test processing order with items not available -> backorder"""
    order = {"status": "processing", "items_available": False}
    assert update_order_status(order) == "backorder"
    assert order["status"] == "backorder"

def test_update_status_other_status():
    """Test order with other status remains unchanged"""
    order = {"status": "shipped"}
    assert update_order_status(order) == "shipped"
    assert order["status"] == "shipped"
    
    order2 = {"status": "delivered"}
    assert update_order_status(order2) == "delivered"
    assert order2["status"] == "delivered"