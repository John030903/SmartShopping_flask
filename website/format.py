from numerize import numerize 

# Add "." for price
def price_format(price):
  price = str(price)
  for i in range(len(price)-3,-1,-3):
    if i != 0:
      price = price[:i] + "." + price[i:]
  return price

def format(items):
  