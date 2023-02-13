from numerize import numerize
import json

def price_format(price):
  price = str(price)
  for i in range(len(price)-3,-1,-3):
    if i != 0:
      price = price[:i] + "." + price[i:]
  return price
  
def tiki_filter(items):
  """
  It takes a list of items, and returns a list of items with the same length, but with less
  information
  
  :param items: The list of items that you want to filter
  :return: A list of dictionaries.
  """
  try:
    filled_items = [dict() for i in range(len(items))]
    PATH = "https://tiki.vn/{}"
    for index, filled_item in enumerate(filled_items):
      filled_item["clickUrl"] = PATH.format(items[index]["url_path"])
      filled_item["thumbnail_url"] = items[index]["thumbnail_url"]
# Converting the rating_average to a number.
      filled_item["rating_average"] = int(float((items[index]["rating_average"]))*100/5)
      filled_item["name"] = items[index]["name"]
      filled_item["price"] = price_format(items[index]["price"])
      try:
        # Converting the number of sold items to a string. For example, if the number of sold items is
        # `12345`, it will return `12.345k`.
        filled_item["sold"] = numerize.numerize(int(items[index]["quantity_sold"]["value"]))
      except:
        filled_item["sold"] = 0
  except:
    return []
  return filled_items

def lazada_filter(items):
  """
  It takes the items from the API and returns a list of dictionaries with the keys: clickUrl,
  thumbnail_url, rating_average, name, price, sold
  
  :param items: The list of items that you want to filter
  :return: A list of dictionaries.
  """
  try:
    filled_items = [dict() for i in range(len(items))]
    PATH = "https://www.lazada.vn/{}"
    for index, filled_item in enumerate(filled_items):
      thumbs0 = items[index]["thumbs"][0]
      filled_item["clickUrl"] = PATH.format(thumbs0["itemUrl"])
      filled_item["thumbnail_url"] = thumbs0["image"]
# Converting the rating_average to a number.
      filled_item["rating_average"] = int(float((items[index]["ratingScore"]))*100/5)
      filled_item["name"] = items[index]["name"]
      filled_item["price"] = price_format(int(float(items[index]["price"])))
# Checking if the number of reviews is empty. If it is empty, it will return 0. If it is not empty, it
# will return the guess of sold.
      if items[index]["review"] == "":
        filled_item["sold"] = 0
      else: 
        filled_item["sold"] = numerize.numerize(int(int(items[index]["review"])/0.3361))
  except:
    return []
  return filled_items

def shopee_filter(scripts):
  """
  It takes a list of items, and returns a list of items with the same length, but with less
  information
  
  :param items: The list of items that you want to filter
  :return: A list of dictionaries.
  """
  try:
    filled_items = [dict() for i in range(len(scripts)-1)]
    for index, filled_item in enumerate(filled_items):
      try:
        item = json.loads(scripts[index+1].text)
        filled_item["clickUrl"] = item["url"]
        filled_item["thumbnail_url"] = item["image"]
# Conv  erting the rating_average to a number.
        filled_item["rating_average"] = int(float((item["aggregateRating"]["ratingValue"]))*100/5)
        print("Not error rating")
        filled_item["name"] = item["name"]
        try:
          filled_item["price"] = price_format(int(float(item["offers"]["price"])))
        except:
          filled_item["price"] = price_format(int(float(item["offers"]["lowPrice"])))
        try:
          # Converting the number of sold items to a string. For example, if the number of sold items is
          # `12345`, it will return `12.345k`.
          # filled_item["sold"] = numerize.numerize(int(items[index]["quantity_sold"]["value"]))
          filled_item["sold"] = numerize.numerize(1000)
        except:
          filled_item["sold"] = 0
      except:
        print("Error")
        continue
  except:
    return []
  return filled_items