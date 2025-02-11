
# Calculate the price after discount, given the price and discount percentage desired.
def calculate_discount(price, discount):
    # check if price and discount are numbers with isinstance
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        # raise a ValueError if price or discount are not numbers
        raise ValueError("Price and discount must numbers.")
    if price < 0:
        # raise a ValueError if price is less than 0
        raise ValueError("Invalid price entered.")
    if discount < 0 or discount > 100:
        # raise a ValueError if discount is less than 0 or greater than 100
        raise ValueError("Invalid discount entered")
    # calculates the price divided by 100 and then multiplied by the discount
    price_after_discount = price - (price * discount / 100)
    # round to 2 decimal places
    return round(price_after_discount, 2)



print(f"Price after discount: {calculate_discount(200, 20)}")
print(f"Price after discount: {calculate_discount(50, 50)}")