Using built function, code is compact but not that performant.
-------------------------------------------------------------
def calculate_total_price2(prices, discount):
  if discount > 100 or discount < 1:
    raise ValueError("Discount must be between 1 and 100")

  products_length = len(prices)
  if products_length > 100 or products_length < 1:
    raise ValueError("Products list size must be between 1 and 100")  

  total_price = sum(prices)
  expensive_price = max(prices)
  least_price = min(prices)

  if expensive_price > 100000 or least_price < 1:
    raise ValueError("Product price must be between 1 and 100000")

  discount_amount = expensive_price * (discount / 100)
  
  return int(total_price - discount_amount)