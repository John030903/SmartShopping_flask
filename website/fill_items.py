# from numerize import numerize
import json
import pandas as pd

# def price_format(price):
#   price = str(price)
#   for i in range(len(price)-3,-1,-3):
#     if i != 0:
#       price = price[:i] + "." + price[i:]
#   return price
  
def tiki_filter(items):
  """
  It takes a list of items, and returns a dataframe with the following columns: click_url,
  thumbnail_url, star_average, name, sold, price
  
  :param items: The list of items that you want to filter
  :return: A dataframe with the following columns: click_url, thumbnail_url, star_average, name, sold,
  price.
  """
  try:
    total = len(items)
    columns = ['click_url', 'thumbnail_url', 'star_average', 'name', 'sold', 'price']
    filled_items = pd.DataFrame(columns=columns, index=range(total))
    PATH = "https://tiki.vn/{}"
    # for index, filled_item in enumerate(filled_items):
    for index in range(total):
      click_url = PATH.format(items[index]["url_path"])
      thumbnail_url = items[index]["thumbnail_url"]
      star_average = int(float((items[index]["rating_average"]))*100/5) # Converting the rating_average to a number.
      name = items[index]["name"]
      try:
        # Converting the number of sold items to a string. For example, if the number of sold items is
        # `12345`, it will return `12.345k`.
        # sold = numerize.numerize(int(items[index]["quantity_sold"]["value"]))
        sold = int(items[index]["quantity_sold"]["value"])
      except:
        sold = 0
      # price = price_format(items[index]["price"])
      price = int(items[index]["price"])
      filled_items.iloc[index] = {
        "click_url": click_url,
        "thumbnail_url": thumbnail_url,
        "star_average": star_average,
        "name": name,
        "sold": sold,
        "price": price
      }
  except:
    return pd.DataFrame()
  return filled_items

def lazada_filter(items):
  """
  It takes the `items` list, which is a list of dictionaries, and returns a Pandas DataFrame
  
  :param items: The list of items that you want to filter
  :return: A dataframe with the following columns:
  - click_url
  - thumbnail_url
  - star_average
  - name
  - sold
  - price
  """
  try:
    total = len(items)
    columns = ['click_url', 'thumbnail_url', 'star_average', 'name', 'sold', 'price']
    filled_items = pd.DataFrame(columns=columns, index=range(total))
    PATH = "https://www.lazada.vn/{}"
    for index in range(total):
      thumbs0 = items[index]["thumbs"][0]
      click_url = PATH.format(thumbs0["itemUrl"])
      thumbnail_url = thumbs0["image"]
      star_average = int(float((items[index]["ratingScore"]))*100/5) 
      name = items[index]["name"]
      try:
        # Converting the number of sold items to a string. For example, if the number of sold items is
        # `12345`, it will return `12.345k`.
        # sold = numerize.numerize(int(int(items[index]["review"])/0.3361))
        sold = int(int(items[index]["review"])/0.3361)
      except:
        sold = 0
      price = int(float(items[index]["price"]))
      filled_items.iloc[index] = {
        "click_url": click_url,
        "thumbnail_url": thumbnail_url,
        "star_average": star_average,
        "name": name,
        "sold": sold,
        "price": price
      }
  except:
    return pd.DataFrame()
  return filled_items

def shopee_filter(scripts):
  """
  It takes a list of items, and returns a list of items with the same length, but with less
  information
  
  :param items: The list of items that you want to filter
  :return: A list of dictionaries.
  """
  try:
    # with open('data.json', 'w', encoding='utf-8') as f:
    #     # write JSON data to file
    #     json.dump(json.loads(scripts[1].text), f, ensure_ascii=False)
    # print(json.loads(scripts[1].text))
    filled_items = [dict() for i in range(len(scripts)-1)]
    total = len(scripts)-1
    columns = ['click_url', 'thumbnail_url', 'star_average', 'name', 'sold', 'price']
    filled_items = pd.DataFrame(columns=columns, index=range(total))
    for index in range(total):
      try:
        item = json.loads(scripts[index+1].text)
        click_url = item["url"]
        thumbnail_url = item["image"]
        star_average = int(float((item["aggregateRating"]["ratingValue"]))*100/5)
        name = item["name"]
        try:
          # Converting the number of sold items to a string. For example, if the number of sold items is
          # `12345`, it will return `12.345k`.
          sold = int(int(item["aggregateRating"]["ratingCount"])/0.3361)
        except:
          sold = 0
        try:
          price = int(float(item["offers"]["price"]))
        except:
          price = int(float(item["offers"]["lowPrice"]))
        filled_items.iloc[index] = {
          "click_url": click_url,
          "thumbnail_url": thumbnail_url,
          "star_average": star_average,
          "name": name,
          "sold": sold,
          "price": price
        }
      except:
        continue
  except:
    return pd.DataFrame()
  return filled_items