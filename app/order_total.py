"""Harbor Street Bakery: order totals for the online order page (course sample code)."""
 
DOZEN_DISCOUNT_PERCENT = 10  # 10 percent off an order of 12 or more of one item
 
 
def order_total(price_cents, quantity):
    """Return the order total in cents."""
    if quantity < 1:
        raise ValueError("quantity must be at least 1")
    total = price_cents * quantity
    if quantity >= 12:
        total = total - total * DOZEN_DISCOUNT_PERCENT // 100
    return total
