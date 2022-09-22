Total price calculation using built in functions with consideration for multiple items with same max price. Eg. User buys most expensive product multiple times [10,20,100,4,100,5].
-------------------------------------------------------------
def calculate_total_price2_duplicate(prices, discount):
  if discount > 100 or discount < 0:
    raise ValueError("Discount must be between 0 and 100")

  products_length = len(prices)
  if products_length > 100 or products_length < 1:
    raise ValueError("Products list size must be between 1 and 100")  

  total_price = sum(prices)
  expensive_price = max(prices)
  least_price = min(prices)

  if expensive_price > 100000 or least_price < 1:
    raise ValueError("Product price must be between 1 and 100000")

  expensive_price_frequency = 0
  for price in prices:
      if price == expensive_price:
        expensive_price_frequency += 1

  discount_amount = expensive_price_frequency * (expensive_price * (discount / 100))
  
  return int(total_price - discount_amount)
