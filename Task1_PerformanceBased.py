Total price calculation with good performance
------------------------------------------------
def calculate_total_price(prices, discount):
  if discount > 100 or discount < 1:
    raise ValueError("Discount must be between 1 and 100")

  products_length = len(prices)
  if products_length > 100 or products_length < 1:
    raise ValueError("Products list size must be between 1 and 100")  

  total_price = 0
  expensive_price = prices[0]
  
  for price in prices:
    if price < 1:
      raise ValueError("Product price must be greater than 0")

    total_price += price
    if price > expensive_price:
      expensive_price = price

  if expensive_price > 100000:
    raise ValueError("Product price must be less than 100000")

  discount_amount = expensive_price * (discount / 100)
  
  return int(total_price - discount_amount)